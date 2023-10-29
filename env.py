from platform import system
import os


def init_env():
    system_name = system()

    if system_name == "Linux":
        os.environ["TERM"] = "linux"
        os.environ["TERMINFO"] = "/etc/terminfo"
    else:
        pass
