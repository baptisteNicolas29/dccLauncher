import os
import subprocess
import importlib.util


def launch(dcc_exe: str, environ, project_path):
    print(dcc_exe, environ)
    """this function launch defined dcc"""

    maya_exe: str = r"C:\Program Files\Autodesk\Maya2022\bin\maya.exe"
    project_path: str = "F:\\1_infographie\\projects\\custom_test"
    environ = os.environ.copy()

    module_location = os.path.join(project_path, '_pipeline', '_project', 'launcher_hook.py')
    spec = importlib.util.spec_from_file_location("hook", module_location)
    hook = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hook)
    environ = hook.environ('maya', 'prod')

    subprocess.Popen(maya_exe, env=environ)
