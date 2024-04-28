from typing import Dict, Any, List
import os
import json


def get_source_path() -> str:
    root_path = os.path.dirname(__file__)
    root_path = os.path.dirname(root_path)
    root_path = os.path.dirname(root_path)
    return os.path.join(root_path, "src")


def load_config() -> Dict[str, Any]:
    config_path = os.path.join(get_source_path(), "config.json")
    with open(config_path, 'r') as file:
        data = json.load(file)
    return data


def get_dcc() -> List[str]:
    conf = load_config()
    return list(conf["DCC"].keys())


def get_dcc_config(dcc: str) -> Dict[str, Any]:
    return load_config()["DCC"].get(dcc, {})


def get_projects() -> Dict[str, Any]:
    return list(load_config()["projects"].keys())


def get_project_by_name(name: str) -> str:
    return load_config()['projects'].get(name, None)
