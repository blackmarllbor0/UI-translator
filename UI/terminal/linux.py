import npyscreen, curses
import UI.terminal.components.input as Input, UI.terminal.components.output as Output


class MainForm(npyscreen.FormBaseNew):
    def create(self):
        self.add_event_hander("event_value_edited", self.event_value_edited)

        handlers = {
            "^Q": self.exit_func,
            curses.ascii.alt(curses.ascii.NL): self.inputbox_clear,
        }

        self.add_handlers(handlers)

        height, width = self.useable_space()
        self.input = self.add(Input.Input, name="Enter text:", max_height=height // 2)
        self.output = self.add(Output.Output, footer="Result", editable=False)

    def event_value_edited(self, event):
        self.output.value = self.input.value
        self.output.display()

    def inputbox_clear(self, _input):
        self.input.value = self.output.value = ""
        self.input.display()
        self.output.display()

    def exit_func(self, _input):
        exit(0)
