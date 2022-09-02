"""WhoSays module."""
import datetime
import logging
import re
import time

from mininode import MiniNode
from mininode.crypto import create_private_key
from officy import JsonFile

from whosays.config import *

logger = logging.getLogger()


class WhoSays:
    """rum bot，搜寻目标用户在某些种子网络的动态并转发到指定种子网络"""

    def __init__(
        self,
        name=None,
        seeds=None,
        whos_keys=None,
        toshare_group_seed=None,
    ):
        self.name = name or NAME
        self.seeds = seeds or ORIGIN_SEEDS
        self.whos_keys = whos_keys or JsonFile(WHOS_KEYS_FILE).read({})
        self.rum_toshare = MiniNode(toshare_group_seed or TOSHARE_GROUP_SEED)

    @staticmethod
    def init_whos_keys(name=None, seeds=None):
        """初始化获取 whos_keys 信息，但返回结果需要人工筛选，以判断某些 pubkey 是否为目标用户。"""
        name = name or NAME
        seeds = seeds or ORIGIN_SEEDS
        whos_keys = {}
        for group_id in seeds:
            seed = seeds[group_id]["seed"]
            rum = MiniNode(seed)
            whos_keys[group_id] = {}

            trxs = rum.api.get_all_contents(trx_types=["person"])
            for trx in trxs:
                print(datetime.datetime.now(), trx["TrxId"])
                _name = trx.get("Content", {}).get("name", "")
                if _name.lower().find(name.lower()) >= 0:
                    _pubkey = trx.get("Publisher")
                    print(_pubkey, _name)
                    if _pubkey and _pubkey not in whos_keys[group_id]:
                        whos_keys[group_id][_pubkey] = {
                            "name": _name,
                            "pubkey": _pubkey,
                            "pvtkey": create_private_key(),
                            "start_trx": None,
                        }

        JsonFile(WHOS_KEYS_FILE).write(whos_keys, is_cover=False)
        return whos_keys

    def init_profile(self):
        """为每个 pubkey 在 toshare_group 所映射的 pvtkey 设置昵称，并发布第一条内容：宣告自己为 bot 账号。"""
        for group_id in self.seeds:
            group_name = self.seeds[group_id]["group_name"]
            seed = self.seeds[group_id]["seed"]
            for pubkey in self.whos_keys[group_id]:
                info = self.whos_keys[group_id][pubkey]
                name = info["name"]
                pvtkey = info["pvtkey"]
                pubkey = info["pubkey"][-10:-2]
                resp = self.rum_toshare.api.update_profile(pvtkey, name=f"{name}@{group_name}")
                logger.info("update_profile: %s", resp)
                _text = f"当前账号为 bot 自动转发 {name}({pubkey}) 在种子网络 {group_name} 的内容及交互，原始数据可加入种子网络查询：\n{seed}"
                resp = self.rum_toshare.api.send_content(pvtkey, content=_text)
                logger.info("send_content: %s", resp)
        return True

    def get_profiles(self, nicknames=None):
        """获取其它用户的昵称，以用于动态的生成"""
        nicknames = nicknames or JsonFile(NICKNAMES_FILE).read({})
        for group_id in self.seeds:
            seed = self.seeds[group_id]["seed"]
            rum_origin = MiniNode(seed)
            if group_id not in nicknames:
                nicknames[group_id] = {"users": {"progress_tid": None}}
            users = nicknames[group_id]["users"]
            nicknames[group_id]["users"] = rum_origin.api.get_profiles(types=("name",), users=users)
        JsonFile(NICKNAMES_FILE).write(nicknames, is_cover=True)
        return nicknames

    def send_to_rum(self):
        """搜寻并生成目标用户的动态，发送到指定种子网络"""
        whos_keys = JsonFile(WHOS_KEYS_FILE).read()
        nicknames_data = self.get_profiles()
        for group_id in self.seeds:
            seed = self.seeds[group_id]["seed"]
            rum_origin = MiniNode(seed)
            nicknames = nicknames_data[group_id]["users"]
            for pubkey in whos_keys[group_id]:
                info = whos_keys[group_id][pubkey]
                trxs = rum_origin.api.get_all_contents(senders=[pubkey], start_trx=info["start_trx"])
                for trx in trxs:
                    params = rum_origin.api.trx_retweet_params(trx, nicknames)
                    if "content" in params:
                        # 移除 content 中首行的名字和时间戳
                        _lines = params["content"].split("\n")
                        if _lines[0].find("说：") >= 0:
                            _lines = _lines[1:]
                        else:
                            _pttn = r"^.*? 202\d-\d\d-\d\d \d\d:\d\d:\d\d.*?"
                            _lines[0] = re.sub(_pttn, "", _lines[0])

                        params["content"] = "\n".join(_lines)
                    resp = self.rum_toshare.api.send_content(info["pvtkey"], timestamp=int(trx["TimeStamp"]), **params)
                    print(datetime.datetime.now(), "send_to_rum", trx["TrxId"], resp["trx_id"])
                    if "trx_id" in resp:
                        whos_keys[group_id][pubkey]["start_trx"] = trx["TrxId"]
                        JsonFile(WHOS_KEYS_FILE).write(whos_keys)
                        time.sleep(1)
