from typing import List
from pathlib import Path

from core.project.shot import Shots
from core.project.asset import Assets
from core.project.environ import Environ
from core.project.departement import Departement


class Project:

    PIPELINE_FOLDER: str = ".pipeline"
    ENVIRON_PATH: str = "config/environ"
    CONTENT_PATH: str = "config/content"
    PROJECT_ENVIRON: str = "project.json"
    ASSETS_CONFIG: str = "assets.json"
    SHOTS_CONFIG: str = "shots.json"

    def __init__(self, path: str) -> None:
        self.__path = Path(path)
        self.__departement: List[Departement] = []

    @property
    def path(self) -> Path:
        """this method represent the location path off the project
        :rtype: pathlib.Path
        :return: path represent the project location
        """
        if not self.__path.exists():
            raise NotADirectoryError("{self.__path} does not exists")
        return self.__path

    @property
    def environ(self) -> Environ:
        return Environ(
                self.__path /
                self.PIPELINE_FOLDER /
                self.ENVIRON_PATH
            )

    @property
    def assets(self) -> Assets:
        return Assets(self.path / self.CONTENT_PATH / self.ASSETS_CONFIG)

    @property
    def shots(self) -> Shots:
        return Shots(self.path / self.CONTENT_PATH / self.SHOTS_CONFIG)
