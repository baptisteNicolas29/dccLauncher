import os
import json
from pathlib import Path
from typing import Any, Dict, List


def getEnvionFromPaths(paths: List[Path]) -> Dict[str, Any]:

    data: Dict[str, Any] = {}

    for path in paths:
        with path.open() as f:
            data.update(json.loads(f.read()))

    return getEnviron(data)


def getEnviron(data: Dict[str, Any]) -> Dict[str, Any]:

    env = os.environ.copy()
    for key, value in data.items():
        if isinstance(value, list):
            value = value.join(";")
        env[key] = value

    return env
