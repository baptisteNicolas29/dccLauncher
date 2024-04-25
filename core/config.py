from typing import Dict, Any, List
import os
import json

import os
import json
from typing import List
from string import Formatter


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
    if not os.path.exists(os.path.join(project_path, '_pipeline', '_project')):
        raise NameError(f"folder : {project_path} is not conform")

    paths.remove("_project")

    if 'prod' in paths:
        paths.remove('prod')
        paths.insert(0, 'prod')

    return paths


def compute_environ(dcc: str, env: str, project_path: str):

    custom_environ = os.environ.copy()
    project_data, environ_data = None, None

    project_environ_path = os.path.join(project_path, '_pipeline', '_project', 'project.json')
    dcc_environ_path = os.path.join(project_path, '_pipeline', '_project', f'{dcc}.json')

    if not os.path.exists(project_environ_path):
        raise NameError("fail to found {project_environ_path}")

    if not os.path.exists(dcc_environ_path):
        raise NameError("fail to found {dcc_environ_path}")

    with open(project_environ_path, "r") as file:
        project_data = json.load(file)

    with open(dcc_environ_path, "r") as file:
        environ_data = json.load(file)

    custom_environ["PROJECT_ROOT"] = project_path
    custom_environ["PIPELINER_ENVIRON"] = env
    custom_environ["PIPELINER_DCC"] = dcc

    for key, path in project_data.items():
        print("from project", key, path)
        custom_environ[key] = path.format(PROJECT_ROOT=project_path)

    for key, path in environ_data.items():
        print("from maya", key, path)
        new_dict = dict()
        format_key = Formatter().parse(path)
        for _, k, _, _ in format_key:
            new_dict[k] = custom_environ.get(k, None)

        custom_environ[key] = path.format(**new_dict)

    return custom_environ

