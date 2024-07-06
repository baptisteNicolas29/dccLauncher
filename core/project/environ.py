import os
from typing import Union
from pathlib import Path

from core.config import environ as env


class Environ:

    def __init__(self, path: Union[str, Path]):

        if isinstance(path, str):
            self.__path = Path(path)

        else:
            self.__path = path

    @property
    def path(self) -> Path:
        """this method represent the location path off the project
        :rtype: pathlib.Path
        :return: path represent the project location
        """
        return self.__path

    @property
    def projectEnvPath(self) -> Path:
        """ this method represent the location path off the project environ
        :rtype: pathlib.Path
        :return: path represent the project environ location
        """
        env_path = self.__path / "project.json"
        return env_path

    def dccEnvPath(self, dcc: str) -> Path:
        """ this method represent the location path off the project environ
        :rtype: pathlib.Path
        :return: path represent the project environ location
        """
        env_path = self.__path / f"{dcc}.json"
        return env_path

    @property
    def projectEnv(self) -> os._Environ:
        """get environement of the project
        :rtype: os._Environ
        :return: environement of the project
        """
        if not self.projectEnvPath.exists():
            raise FileNotFoundError(
                    "fail to found config for environement"
                    "\n{self.projectEnvPath}"
                    )
        customEnv = env.getEnvionFromPaths([self.projectEnvPath])
        customEnv["folder_root"] = str(self.path)
        return customEnv

    def dccEnv(self, dcc: str) -> os._Environ:
        """get environement of the project
        :rtype: os._Environ
        :return: environement of the project
        """
        if not self.projectEnvPath.exists():
            raise FileNotFoundError(
                    "fail to found config for environement"
                    "\n{self.projectEnvPath}"
                    )

        if not self.dccEnvPath(dcc).exists():
            raise FileNotFoundError(
                    "fail to found config for environement"
                    "\n{self.dccEnvPath(dcc)}"
                    )

        customEnv = env.getEnvionFromPaths(
                [
                    self.dccEnvPath,
                    self.projectEnvPath
                ]
            )
        customEnv["folder_root"] = str(self.path)
        return customEnv
