import subprocess

from launcher.core import configuration
from launcher.core import project


def launch(dcc: str, environ, project_path: str):
    """this function launch defined dcc"""

    environnement = project.compute_environ(dcc, environ, project_path)
    dcc = configuration.get_dcc_config(dcc)

    if not dcc:
        raise NameError(f'fail to found {dcc} in config file')

    dcc_exe = dcc["versions"][dcc["default"]]

    subprocess.Popen(dcc_exe, env=environnement)
