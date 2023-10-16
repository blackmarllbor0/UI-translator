from curses import wrapper
from UI.terminal.linux import LinuxTerminalUI


def main(stdscr):
    editor = LinuxTerminalUI(stdscr)
    editor.run()


if __name__ == "__main__":
    wrapper(main)
