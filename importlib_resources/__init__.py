import importlib
import io
import os.path
import sys
from typing import Union
from typing.io import BinaryIO

if sys.version_info >= (3, 6):
    from os import fspath as _fspath
    Path = Union[str, os.PathLike]
else:
    Path = Union[str]
    def _fspath(path):
        if isinstance(path, (str, bytes)):
            return path

        path_type = type(path)
        try:
            path = path_type.__fspath__(path)
        except AttributeError:
            if hasattr(path_type, '__fspath__'):
                raise
        else:
            if isinstance(path, (str, bytes)):
                return path
            else:
                raise TypeError("expected __fspath__() to return str or bytes, "
                                "not " + type(path).__name__)

        raise TypeError("expected str, bytes or os.PathLike object, not "
                        + path_type.__name__)


def _get_package(package_name):
    module = importlib.import_module(package_name)
    if module.__spec__.submodule_search_locations is None:
        raise TypeError("{!r} is not a package".format(package_name))
    else:
        return module


def _normalize_path(path):
    path = _fspath(path)
    if os.path.isabs(path):
        raise ValueError("{!r} is absolute".format(path))
    normalized_path = os.path.normpath(path)
    if normalized_path.startswith(".."):
        raise ValueError("{!r} attempts to traverse past package".format(path))
    else:
        return normalized_path


def open(package_name: str, path: Path) -> BinaryIO:
    """Return a file-like object opened for binary-reading of the resource."""
    normalized_path = _normalize_path(path)
    package = _get_package(package_name)
    package_path = os.path.dirname(os.path.abspath(package.__spec__.origin))
    full_path = os.path.join(package_path, normalized_path)
    data = package.__spec__.loader.get_data(full_path)
    return io.BytesIO(data)
