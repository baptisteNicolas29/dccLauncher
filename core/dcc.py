import os
import subprocess
import importlib.util
from pprint import pprint

from core import config


def launch(dcc: str, environ, project_path: str):
    """this function launch defined dcc"""

    environnement = config.compute_environ(dcc, environ, project_path)
    dcc_exe = list(config.load_config()["DCC"].get(dcc, {}).get("versions").values())[0]
    print(dcc_exe)
    pprint(environ)

    subprocess.Popen(dcc_exe, env=environnement )
