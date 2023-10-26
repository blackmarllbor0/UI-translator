from abc import ABC

from storage import StorageService


class Translator(ABC):
    def __init__(self, storage_service: StorageService):
        super().__init__()
        self.storage_service = storage_service
        self.src_lang = storage_service.storage["lang"]["src"]
        self.dest_lang = storage_service.storage["lang"]["dest"]

    @classmethod
    def translate(cls, text: str) -> str:
        pass
