from os import PathLike, remove
from os.path import exists, isdir
from shutil import rmtree

from click import echo, style


__version__ = "0.0.1-dev0"


def clean(path: list[str | PathLike], verbose=False):
    """Removes all given Path-Objects, meaning files are deleted and
    directorys are removed recurlivly.

    Args:
        `path` (list[str|PathLike]): List of Paths to delete.
        `verbose` (bool, optional): If set to `True`, prints informations to the screen.
    """
    for p in path:
        if not exists(p):
            if verbose:
                echo(f'{style("skip", fg="yellow")}: {p}')
            continue
        if isdir(p):
            if not p.endswith("/"):
                p += "/"
            if verbose:
                echo(f'{style("dir", fg="bright_cyan")}:  {p}')
            rmtree(p)
        else:
            if verbose:
                echo(f'{style("file", fg="blue")}: {p}')
            remove(p)
