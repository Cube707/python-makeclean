from os import PathLike, remove
from os.path import exists, isdir
from shutil import rmtree

import click


__version__ = "0.0.1-dev0"


@click.command()
@click.help_option("--help", "-h")
@click.option("--verbose", "-v", is_flag=True, default=False)
@click.option("--version", "-V", is_flag=True, default=False)
@click.argument("PATH", nargs=-1, type=click.Path())
def main(path, verbose, version):
    """This utility is meant for use in makefiles as the clean target or similar usecases.
    It takes an arbitray number of PATH objects and removes them if they exists.
    Folders will be remove recursivly."""
    if version:
        print(f"makeclean.py v{__version__}")
        return
    clean(path, verbose)


def clean(path: list[str|PathLike], verbose=False):
    """Removes all given Path-Objects, meaning files are deleted and
    directorys are removed recurlivly.

    Args:
        `path` (list[str|PathLike]): List of Paths to delete.
        `verbose` (bool, optional): If set to `True`, prints informations to the screen.
    """
    for p in path:
        if not exists(p):
            if verbose:
                click.echo(f'{click.style("skip", fg="yellow")}: {p}')
            continue
        if isdir(p):
            if not p.endswith("/"):
                p += "/"
            if verbose:
                click.echo(f'{click.style("dir", fg="bright_cyan")}:  {p}')
            rmtree(p)
        else:
            if verbose:
                click.echo(f'{click.style("file", fg="blue")}: {p}')
            remove(p)
