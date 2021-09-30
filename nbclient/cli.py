import logging
import pathlib
from textwrap import dedent

import nbformat
from jupyter_core.application import JupyterApp, base_aliases, base_flags
from traitlets import Bool, Integer, List, Unicode, default
from traitlets.config import catch_config_error

from nbclient import __version__

from .client import NotebookClient
from .exceptions import CellExecutionError

nbclient_aliases = {}
nbclient_aliases.update(base_aliases)
nbclient_aliases.update(
    {
        'timeout': 'NbClientApp.timeout',
        'startup_timeout': 'NbClientApp.startup_timeout',
        'kernel_name': 'NbClientApp.kernel_name',
    }
)

nbclient_flags = {}
nbclient_flags.update(base_flags)
nbclient_flags.update(
    {
        'allow-errors': (
            {
                'NbClientApp': {
                    'allow_errors': True,
                },
            },
            "Errors are ignored and execution is continued until the end of the notebook.",
        ),
    }
)


class NbClientApp(JupyterApp):
    """
    An application used to execute a notebook files (``*.ipynb``)
    """

    version = __version__
    name = 'jupyter-execute'
    aliases = nbclient_aliases
    flags = nbclient_flags

    description = Unicode("An application used to execute a notebook files (*.ipynb)")
    notebook = List([], help="Path of notebooks to convert").tag(config=True)
    timeout: int = Integer(
        None,
        allow_none=True,
        help=dedent(
            """
            The time to wait (in seconds) for output from executions.
            If a cell execution takes longer, a TimeoutError is raised.
            ``-1`` will disable the timeout.
            """
        ),
    ).tag(config=True)
    startup_timeout: int = Integer(
        60,
        help=dedent(
            """
            The time to wait (in seconds) for the kernel to start.
            If kernel startup takes longer, a RuntimeError is
            raised.
            """
        ),
    ).tag(config=True)
    allow_errors: bool = Bool(
        False,
        help=dedent(
            """
            When a cell raises an error the default behavior is that
            execution is stopped and a `CellExecutionError`
            is raised.
            If this flag is provided, errors are ignored and execution
            is continued until the end of the notebook.
            """
        ),
    ).tag(config=True)
    skip_cells_with_tag: str = Unicode(
        'skip-execution',
        help=dedent(
            """
            Name of the cell tag to use to denote a cell that should be skipped.
            """
        ),
    ).tag(config=True)
    kernel_name: str = Unicode(
        '',
        help=dedent(
            """
            Name of kernel to use to execute the cells.
            If not set, use the kernel_spec embedded in the notebook.
            """
        ),
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
            timeout=self.timeout,
            startup_timeout=self.startup_timeout,
            skip_cells_with_tag=self.skip_cells_with_tag,
            allow_errors=self.allow_errors,
            kernel_name=self.kernel_name,
            resources={'metadata': {'path': path}},
        )
        try:
            # Run it
            client.execute()
        except CellExecutionError:
            # If there's an error, print it to the terminal.
            msg = f"Error executing {input_path}"
            self.log.error(msg)
            # And then raise it too
            raise


main = launch_new_instance = NbClientApp.launch_instance
