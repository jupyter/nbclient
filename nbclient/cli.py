# -*- coding: utf-8 -*-
"""
A command-line interface for running Jupyter Notebooks.
Usage: cli.py [OPTIONS] [NOTEBOOK_PATHS]...
    Executes Jupyter Notebooks from the command line.

    Expects one or more file paths input as arguments.

    Errors are raised and printed to the console.

    Example:
        $ python run.py ./src/notebooks.ipynb

    Options:
        --help  Show this message and exit.
"""
import click
import pathlib
import nbformat
from .client import NotebookClient
from .exceptions import CellExecutionError


@click.group(help="Run Jupyter Notebooks from the command line")
def cli():
    pass


@cli.command(help="Execute a notebook")
@click.argument('notebook_path', nargs=1, type=click.Path(exists=True))
@click.option('-o', '--output', default=None, help='Where to output the result')
@click.option('-t', '--timeout', default=600, help='How long the script should run before it times out')
@click.option('--allow-errors/--no-allow-errors', default=False)
@click.option('--force-raise-errors/--no-force-raise-errors', default=True)
def execute(notebook_path, output, timeout, allow_errors, force_raise_errors):
    """
    Executes Jupyter Notebooks from the command line.

    Expects one or more file paths input as arguments.

    Errors are raised and printed to the console.

    Example:

        $ python run.py ./src/notebooks.ipynb
    """
    # Get the file name
    name = notebook_path.replace(".ipynb", "")

    # Get its parent directory so we can add it to the $PATH
    path = pathlib.Path(notebook_path).parent.absolute()

    # Set the intput file paths
    input_path = f"{name}.ipynb"

    # Open up the notebook we're going to run
    with open(input_path) as f:
        nb = nbformat.read(f, as_version=4)

    # Configure nbclient to run the notebook
    client = NotebookClient(
        # What we want it to run
        nb,
        timeout=timeout,
        kernel_name='python3',
        allow_errors=allow_errors,
        force_raise_errors=force_raise_errors,
        # Here's where the path gets set
        resources={'metadata': {'path': path}}
    )
    try:
        # Run it
        client.execute()
    except CellExecutionError:
        # If there's an error, print it to the terminal.
        msg = f"Error executing {input_path}.\n"
        click.echo(msg)
        # And then raise it too
        raise
    finally:
        if output:
            # Once all that's done, write out the output notebook to the filesystem
            with open(output, mode='w', encoding='utf-8') as f:
                nbformat.write(nb, f)


if __name__ == '__main__':
    cli()
