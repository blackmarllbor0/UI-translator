import curses


class LinuxTerminalUI:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.input_window = None
        self.output_window = None

    def setup_window(self):
        curses.curs_set(1)  # on input cursor
        self.stdscr.clear()

        height, width = self.stdscr.getmaxyx()  # get window size

        middle = width // 2

        # create a window to input text
        self.input_window = curses.newwin(height, middle, 0, 0)
        self.input_window.border(0)

        # create a window to output text
        self.output_window = curses.newwin(height, middle, 0, middle)
        self.output_window.border(0)

        self.input_window.refresh()
        self.output_window.refresh()

    def edit_text(self):
        curses.curs_set(1)
        input_text = ""

        while True:
            key = self.input_window.getch()

            if key == curses.KEY_ENTER:
                self.output_window.clear()
                self.output_window.addstr(1, 1, input_text)
                self.output_window.refresh()
                # input_text = ""
            elif key == curses.KEY_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text = chr(key)

            self.input_window.clear()
            self.input_window.addstr(1, 1, input_text)
            self.input_window.refresh()

    def run(self):
        self.setup_window()
        self.edit_text()
