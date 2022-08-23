import click

from . import __version__, clean


@click.command()
@click.help_option("--help", "-h")
@click.option("--verbose", "-v", is_flag=True, default=False)
@click.option("--version", "-V", is_flag=True, default=False)
@click.argument("PATH", nargs=-1, type=click.Path())
def cli(path, verbose, version):
    """This utility is meant for use in makefiles as the clean target or similar
    usecases. It takes an arbitray number of PATH objects and removes them if they
    exists. Folders will be remove recursivly."""
    if version:
        print(f"makeclean.py v{__version__}")
        return
    clean(path, verbose)


if __name__ == "__main__":
    cli()
