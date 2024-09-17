"""Constants for the project."""

from typing import Any

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

__version__: str | Any = metadata.version(__package__ or __name__)
__desc__: str | Any = metadata.metadata(__package__ or __name__)["Summary"]
PACKAGE: str | Any = metadata.metadata(__package__ or __name__)["Name"]
GITHUB: str | Any = metadata.metadata(__package__ or __name__)["Home-page"]

MAX_TIMEOUT = 5

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
PROFILE = False
