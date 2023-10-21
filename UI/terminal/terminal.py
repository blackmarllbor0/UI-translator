import npyscreen
from UI.terminal.get_ui_by_oc import get_UI_by_user_OC


class TerminalUI(npyscreen.StandardApp):
    def __init__(self):
        super().__init__()
        self._form = get_UI_by_user_OC()

    def onStart(self):
        self.addForm("MAIN", self._form, name="Translator")
