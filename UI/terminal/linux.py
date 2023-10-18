import curses


class LinuxTerminalUI:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.input_window = None
        self.output_window = None

    def setup_window(self):
        curses.curs_set(1)  # On input cursor
        self.stdscr.clear()

        max_height, max_width = self.stdscr.getmaxyx()  # get window size

        middle = max_width // 2

        # create window to input text
        self.input_window = curses.newwin(max_height - 2, middle, 1, 1)
        self.input_window.border(0)

        # create window to output text
        self.output_window = curses.newwin(
            max_height - 2, max_width - middle - 2, 1, middle + 1
        )
        self.output_window.border(0)

        self.input_window.refresh()
        self.output_window.refresh()

    def edit_text(self):
        curses.curs_set(1)
        input_text = ""

        while True:
            key = self.input_window.getch()

            if key == 10:  # Enter key
                self.output_window.clear()
                self.output_window.refresh()  # Обновить окно вывода
                self.output_window.addstr(1, 1, input_text)
                input_text = ""
            elif key == curses.KEY_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += chr(key)

            self.input_window.clear()
            self.input_window.addstr(1, 1, input_text)
            self.input_window.refresh()

    def run(self):
        self.setup_window()
        self.edit_text()


if __name__ == "__main__":
    curses.wrapper(LinuxTerminalUI)
