from typing import Dict, Any, List
import os
import json


def get_source_path() -> str:
    root_path = os.path.dirname(__file__)
    root_path = os.path.dirname(root_path)
    return os.path.join(root_path, "src")


def load_config() -> Dict[str, Any]:

    config_path = os.path.join(get_source_path(), "config.json")

    with open(config_path, 'r') as file:
        data = json.load(file)

    return data


def get_project_environ(project_path: str) -> List[str]:
    paths = os.listdir(os.path.join(project_path, '_pipeline'))
    if '_project' not in paths:
        raise NameError(f"folder : {project_path} is not conform")

    paths.remove("_project")

    if 'prod' in paths:
        paths.remove('prod')
        paths.insert(0, 'prod')

    return paths
