from googletrans import Translator
from storage import StorageService

import API.translator as MainTranslator


class GoogleTranslator(MainTranslator.Translator):
    def __init__(self, storage_service: StorageService):
        super().__init__(storage_service)
        self.translator = Translator()
        self.translator.raise_Exception = True

    def translate(self, text: str) -> str:
        translate_result = self.translator.translate(
            text=text, src=self.src_lang, dest=self.dest_lang
        ).text

        return translate_result
