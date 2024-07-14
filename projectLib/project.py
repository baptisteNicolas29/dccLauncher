from typing import Union
from pathlib import Path


class Project:

    def __init__(self, path: Union[str, Path]) -> None:
        self.__path = path if isinstance(path, Path) else Path(path)
        self.__assets = {str(x).upper(): x for x in range(5000)}

    def path(self) -> Path:
        return self.__path

    def keys(self) -> None:
        return self.__assets.keys()

    def values(self):
        return self.__assets.values()

    def items(self):
        return self.__assets.items()

    def __getitem__(self, key: str):
        return self.__assets[key]
