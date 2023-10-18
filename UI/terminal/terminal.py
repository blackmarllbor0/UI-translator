from abc import ABC, abstractmethod


class TerminalUI(ABC):
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.input_window = None
        self.outut_window = None

    @abstractmethod
    def setup_window(self):
        pass

    @abstractmethod
    def edit_text(self):
        pass

    def run(self):
        self.setup_window()
        self.edit_text()
