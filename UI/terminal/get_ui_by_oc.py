import UI.terminal.linux as Linux
import platform

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"


def get_UI_by_user_OC():
    system = platform.system()

    if system == WINDOWS:
        # TODO i need to write an impl for windows
        pass
    elif system in (LINUX, MACOS):
        return Linux.MainForm
    else:
        raise NotImplementedError("Platform not supported")
