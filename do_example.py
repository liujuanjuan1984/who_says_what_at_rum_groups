import time

from whosays import WhoSays


# 只有初始化时，才需要。
def init_bot():
    WhoSays.init_whos_keys()
    WhoSays().init_profile()


def send_to_rum():
    while True:
        try:
            WhoSays().send_to_rum()
        except Exception as e:
            print(e)
            time.sleep(1)


if __name__ == "__main__":
    # WhoSays.init_whos_keys()
    # WhoSays().init_profile()
    # WhoSays().send_to_rum()
    pass
