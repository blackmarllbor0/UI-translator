import npyscreen

import UI.terminal.components.input as Input
import UI.terminal.components.output as Output

from exit import Exit
from API.get_translator_by_api import get_translator_by_api


class TerminalUI(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", App, name="Translator")


class App(npyscreen.FormBaseNew):
    def create(self):
        self.translator = get_translator_by_api()

        self.add_event_hander("event_value_edited", self.event_value_edited)
        self.keypress_timeout = 8

        self.add_handlers(
            {
                "^Q": self.exit,  # ctrl+Q
                "^U": self.input_box_clear,  # alt+enter
                "^S": self.swap_lang,  # swap lang
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

        # auto changes lang when input text
        if self.input.footer != self.translator.src_lang:
            self.input.footer = self.translator.src_lang

        self.input.display()
        self.output.display()

    def swap_lang(self, _input):
        input_value = self.input.value
        input_lang = self.input.footer

        if input_lang != "auto" and input_lang.__str__().strip():
            self.input.value = self.output.value
            self.output.value = input_value

            self.translator.set_src_lang(self.output.footer)
            self.translator.set_dest_lang(input_lang)

            self.input.footer = self.translator.src_lang
            self.output.footer = self.translator.dest_lang

        self.input.display()
        self.output.display()

    def exit(self, _input):
        Exit.good()
