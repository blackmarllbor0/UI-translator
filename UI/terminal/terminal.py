import npyscreen

import UI.terminal.components.input as Input
import UI.terminal.components.output as Output

from exit import Exit
from API.get_translator_by_api import get_translator_by_api


class TerminalUI(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", App, name="Translator")


class App(npyscreen.FormBaseNew):
    def __init__(
        self,
        name=None,
        parentApp=None,
        framed=None,
        help=None,
        color="FORMDEFAULT",
        widget_list=None,
        cycle_widgets=False,
        *args,
        **keywords
    ):
        super().__init__(
            name,
            parentApp,
            framed,
            help,
            color,
            widget_list,
            cycle_widgets,
            *args,
            **keywords
        )

    def create(self):
        self.translator = get_translator_by_api()

        self.add_event_hander("event_value_edited", self.event_value_edited)
        self.keypress_timeout = 6

        self.add_handlers(
            {
                "^Q": self.exit,  # ctrl+Q
                "^U": self.input_box_clear,  # alt+enter
            }
        )

        height, width = self.useable_space()

        self.input: Input.Input = self.add(
            Input.Input,
            name="Enter text:",
            footer=self.translator.src_lang,
            max_height=height // 2,
        )

        self.output: Output.Output = self.add(
            Output.Output,
            footer=self.translator.dest_lang,
            name="Result",
            editable=False,
        )

    def event_value_edited(self, _event):
        self.output.value = self.input.value
        self.output.display()

    def input_box_clear(self, _input):
        self.input.value = self.output.value = ""
        self.input.display()
        self.output.display()

    def while_waiting(self):
        if self.input.value is not None and len(self.input.value) > 1:
            translated_text = self.translator.translate(self.input.value)
            self.output.value = translated_text

        self.input.display()
        self.output.display()

    def exit(self, _input):
        Exit.good()
