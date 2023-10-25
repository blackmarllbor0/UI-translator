import shutil
from pathlib import Path
from typing import TypedDict

import yaml

from exit import Exit


class Lang(TypedDict):
    src: str
    dest: str


class Storage(TypedDict):
    lang: Lang
    translate_api: str


class StorageService:
    storage: Storage

    def __init__(self):
        self._path = Path.home() / "translator_storage.yaml"
        self._storage_layout = "storage_layout.yaml"

        self._create_storage()
        self.load_storage()

    def check_file_is_exist(self) -> bool:
        return self._path.exists()

    def _create_storage(self):
        try:
            if not self.check_file_is_exist():
                shutil.copy(self._storage_layout, self._path)
        except SystemError as err:
            Exit.error(err)

    def load_storage(self):
        try:
            with open(self._path, "r") as file:
                data = yaml.safe_load(file)
                self.storage: Storage = data["storage"]
        except SystemError as err:
            Exit.error(err)
