from abc import ABC

from trans.storage import StorageService


class Translator(ABC):
    def __init__(self, storage_service: StorageService):
        super().__init__()
        self.storage_service = storage_service

        sl = storage_service.storage["lang"]["src"]
        dl = storage_service.storage["lang"]["dest"]

        if self._validate_lang(sl):
            self.src_lang = sl.lower()
        else:
            self.src_lang = "auto"

        if self._validate_lang(dl):
            self.dest_lang = dl.lower()
        else:
            self.dest_lang = "en"

    @classmethod
    def translate(cls, text: str) -> str:
        pass

    def set_src_lang(self, lang: str) -> None:
        self.src_lang = "auto" if not self._validate_lang(lang) else lang

    def set_dest_lang(self, lang: str) -> None:
        self.dest_lang = self.dest_lang if not self._validate_lang(lang) else lang

    def _validate_lang(self, lang: str) -> bool:
        return lang.strip() and lang.isalpha()
