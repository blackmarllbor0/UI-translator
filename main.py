from curses import wrapper
from UI.terminal.linux import LinuxTerminalUI
from UI.terminal.get_ui_by_oc import get_UI_by_user_OC


def main(stdscr):
    editor = get_UI_by_user_OC(stdscr)
    editor.run()


if __name__ == "__main__":
    wrapper(main)
