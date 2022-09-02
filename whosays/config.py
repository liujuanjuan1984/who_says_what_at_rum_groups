"""config.py"""
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
WHOS_KEYS_FILE = os.path.join(DATA_DIR, f"whos_pubkeys.json")
NICKNAMES_FILE = os.path.join(DATA_DIR, "groups_nicknames.json")

# the seeds of rum groups where the origin data is from
ORIGIN_SEEDS = {
    "bd119dd3-081b-4db6-9d9b-e19e3d6b387e": {
        "group_name": "去中心推特",
        "group_id": "bd119dd3-081b-4db6-9d9b-e19e3d6b387e",
        "seed": "rum://seed?v=1&e=0&n=0&b=d6C-hoVOR4OG5BsBKTE_jg&c=AaJMQssuPKVMFCMhvK2J7eZwOJHs206vDkcaMM2yIdE&g=vRGd0wgbTbadm-GePWs4fg&k=CAISIQOjS6CoEBv0ZtNcXrajpGCOkRgd2gOaoRvQ%2FtXqhE9xhg%3D%3D&s=MEUCIQC3_AQZFUOMCX66ReLB6SSKleyIkTg1HDyoTclqRiD49AIgat4yVuI626zCnEC69iIsbhvr_xPKi4dDGl1GZ1FRDeg&t=FrTZY_-Njc0&a=%E5%8E%BB%E4%B8%AD%E5%BF%83%E6%8E%A8%E7%89%B9&y=group_timeline&u=http%3A%2F%2F127.0.0.1%3A57772%3Fjwt%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbGxvd0dyb3VwcyI6WyJiZDExOWRkMy0wODFiLTRkYjYtOWQ5Yi1lMTllM2Q2YjM4N2UiXSwiZXhwIjoxODE5NTIyNjc1LCJuYW1lIjoiYWxsb3ctYmQxMTlkZDMtMDgxYi00ZGI2LTlkOWItZTE5ZTNkNmIzODdlIiwicm9sZSI6Im5vZGUifQ.DBPS1eqbHfDWxCaS8BbAhjRM9-WxRLaxgCG4E6GaI70",
    },
}

# the seed of rum group where the data is sent to
TOSHARE_GROUP_SEED = "rum://seed?v=1&e=0&n=0&b=Yth4aa0GQqycj82V-cuhTQ&c=f9U8j3bttDuArJeERORtLv_mtkJqmS0goMV9L_QQxzw&g=s-nzEhnJQC24BOmTLThkOA&k=AuZuU_SlW6wYlnIsFmGnNqJZ2QZFqG6hOu9KLaUnGQ_3&s=lDcucoRkcbe-R0dTV0ruN4B4C1X-g-k21G69cHa8OGFHR_qwRlcXUFiHFZRtJvM6cnW45_oKBJoG6__lcSWJ1wE&t=FxD4-C3MLFw&a=test_huoju2&y=group_timeline&u=http%3A%2F%2F127.0.0.1%3A57772%3Fjwt%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbGxvd0dyb3VwcyI6WyJiM2U5ZjMxMi0xOWM5LTQwMmQtYjgwNC1lOTkzMmQzODY0MzgiXSwiZXhwIjoxODE5NzgyMDA4LCJuYW1lIjoiYWxsb3ctYjNlOWYzMTItMTljOS00MDJkLWI4MDQtZTk5MzJkMzg2NDM4Iiwicm9sZSI6Im5vZGUifQ.8t2ZZUR8XBeDJiiUGa2mWChmzo_tw0J4poQQMefp7pc"

# the name of user profile which to search for
NAME = "BotAsSample"
