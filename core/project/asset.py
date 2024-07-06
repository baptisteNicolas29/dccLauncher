import json
from pathlib import Path


class Assets:
    def __init__(self, config: str) -> None:
        self.__path = config
        self.__data = self.load()

    def load(self):
        if not self.__path.exists():
            return {}

        with self.__path.open() as f:
            data = json.loads(f.read())

        return data

    def save(self): ...


class Asset:
    def __init__(self) -> None:
        ...
