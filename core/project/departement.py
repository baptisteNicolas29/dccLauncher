from typing import Optional, List


class Departement:

    def __init__(
            self,
            name: str,
            task: Optional[List[str]] = []
            ) -> None:
        self.__name = name
        self.__task = task

    @property
    def name(self):
        """The name property."""
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError(
                    f"departement name need to be string not {type(value)}"
                    )
        self.__name = value

    @property
    def task(self) -> List[str]:
        return self.__task

    @task.setter
    def task(self, value: List[str]) -> None:

        if not isinstance(value, list):
            raise TypeError(f"task need to be list got {type(value)} instead")

        for val in value:
            if not isinstance(val, str):
                raise TypeError(
                        f"{val} need to be str got {type(value)} instead"
                        )

        self.__task = value
