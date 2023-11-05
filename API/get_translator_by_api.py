from trans.storage import StorageService
from API.translator import Translator
from API.google_api import GoogleTranslator


def get_translator_by_api() -> Translator:
    storage = StorageService()
    api_service = storage.storage["translate_api"]

    if api_service == "google":
        return GoogleTranslator(storage)
    else:
        print(f"check the translate_api field in your {storage._path}")
