from __future__ import absolute_import

import os
import tempfile
import contextlib

from ._compat import (
    Path, package_spec, FileNotFoundError, ZipPath,
    singledispatch,
    )


def from_package(package):
    """Return a Traversable object for the given package"""
    spec = package_spec(package)
    package_directory = Path(spec.origin).parent
    try:
        archive_path = spec.loader.archive
        rel_path = package_directory.relative_to(archive_path)
        return ZipPath(archive_path, str(rel_path) + '/')
    except Exception:
        pass
    return package_directory


@contextlib.contextmanager
def _tempfile(reader):
    # Not using tempfile.NamedTemporaryFile as it leads to deeper 'try'
    # blocks due to the need to close the temporary file to work on Windows
    # properly.
    fd, raw_path = tempfile.mkstemp()
    try:
        os.write(fd, reader())
        os.close(fd)
        yield Path(raw_path)
    finally:
        try:
            os.remove(raw_path)
        except FileNotFoundError:
            pass


@singledispatch
@contextlib.contextmanager
def as_file(path):
    """
    Given a path-like object, return that object as a
    path on the local file system in a context manager.
    """
    with _tempfile(path.read_bytes) as local:
        yield local


@as_file.register(Path)
@contextlib.contextmanager
def _(path):
    """
    Degenerate behavior for pathlib.Path objects
    """
    yield path