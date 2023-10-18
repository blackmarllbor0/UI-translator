from UI.terminal.terminal import TerminalUI
from UI.terminal.linux import LinuxTerminalUI
import platform

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"


def get_UI_by_user_OC(stdscr) -> TerminalUI:
    system = platform.system()

    if system == WINDOWS:
        # TODO i need to write an impl for windows
        pass
    elif system in (LINUX, MACOS):
        return LinuxTerminalUI(stdscr)
    else:
        raise NotImplementedError("Platform not supported")
