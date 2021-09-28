"""
A command-line interface for running Jupyter Notebooks.

Usage: nblclient [OPTIONS] [NOTEBOOK_PATHS]...
    Executes Jupyter Notebooks from the command line.

    Expects one or more file paths input as arguments.

    Errors are raised and printed to the console.

    Example:
        $ nbclient execute ./src/notebooks.ipynb

    Options:
        --help  Show this message and exit.
"""

import pathlib
import logging
import nbformat
from nbclient import __version__
from .client import NotebookClient
from .exceptions import CellExecutionError
from traitlets import default, Unicode, List
from traitlets.config import catch_config_error
from jupyter_core.application import JupyterApp


class NbClientApp(JupyterApp):
    """
    An application used to execute a notebook files (``*.ipynb``)
    """
    version = __version__
    name = 'jupyter-execute'

    description = Unicode("An application used to execute a notebook files (*.ipynb)")
    notebook = List(
        [],
        help="Path of notebooks to convert"
    ).tag(config=True)

    @default('log_level')
    def _log_level_default(self):
        return logging.INFO

    @catch_config_error
    def initialize(self, argv=None):
        super().initialize(argv)
        self.notebooks = self.get_notebooks()
        for notebook_path in self.notebooks:
            self.run_notebook(notebook_path)

    def get_notebooks(self):
        if self.extra_args:
            notebooks = self.extra_args
        else:
            notebooks = self.notebooks
        return notebooks

    def run_notebook(self, notebook_path):
        # Log it
        self.log.info(f"Executing {notebook_path}")
        
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
            nb,
            timeout=600,
            kernel_name='python3',
            allow_errors=False,
            force_raise_errors=True,
            resources={'metadata': {'path': path}},
        )
        try:
            # Run it
            client.execute()
        except CellExecutionError:
            # If there's an error, print it to the terminal.
            msg = f"Error executing {input_path}.\n"
            self.log.error(msg)
            # And then raise it too
            raise


main = launch_new_instance = NbClientApp.launch_instance
