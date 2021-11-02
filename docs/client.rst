Executing notebooks
===================

.. module:: nbclient.client.guide

Jupyter notebooks are often saved with output cells that have been cleared.
NBClient provides a convenient way to execute the input cells of an
.ipynb notebook file and save the results, both input and output cells,
as a .ipynb file.

In this section we show how to execute a ``.ipynb`` notebook
document saving the result in notebook format. If you need to export
notebooks to other formats, such as reStructured Text or Markdown (optionally
executing them) see `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_.

Executing notebooks can be very helpful, for example, to run all notebooks
in Python library in one step, or as a way to automate the data analysis in
projects involving more than one notebook.

Using the Python API interface
------------------------------

This section will illustrate the Python API interface.

Example
~~~~~~~

Let's start with a complete quick example, leaving detailed explanations
to the following sections.

**Import**: First we import nbformat and the :class:`NotebookClient`
class::

    import nbformat
    from nbclient import NotebookClient

**Load**: Assuming that ``notebook_filename`` contains the path to a notebook,
we can load it with::

    nb = nbformat.read(notebook_filename, as_version=4)

**Configure**: Next, we configure the notebook execution mode::

    client = NotebookClient(nb, timeout=600, kernel_name='python3', resources={'metadata': {'path': 'notebooks/'}})

We specified two (optional) arguments ``timeout`` and ``kernel_name``, which
define respectively the cell execution timeout and the execution kernel.
Usually you don't need to set these options, but these and other options are
available to control execution context. Note that ``path`` specifies
in which folder to execute the notebook.

**Execute/Run**: To actually run the notebook we call the method
``execute``::

    client.execute()

Hopefully, we will not get any errors during the notebook execution
(see the last section for error handling). This notebook will
now have its cell outputs populated with the result of running
each cell.

**Save**: Finally, save the resulting notebook with::

    nbformat.write(nb, 'executed_notebook.ipynb')

That's all. Your executed notebook will be saved in the current folder
in the file ``executed_notebook.ipynb``.

Execution arguments (traitlets)
-------------------------------

The arguments passed to :class:`NotebookClient` are configuration options
called `traitlets <https://traitlets.readthedocs.io/en/stable>`_.
There are many cool things about traitlets. For example,
they enforce the input type, and they can be accessed/modified as
class attributes.

Let's now discuss in more detail the two traitlets we used.

The ``timeout`` traitlet defines the maximum time (in seconds) each notebook
cell is allowed to run, if the execution takes longer an exception will be
raised. The default is 30 s, so in cases of long-running cells you may want to
specify an higher value. The ``timeout`` option can also be set to ``None``
or ``-1`` to remove any restriction on execution time.

The second traitlet, ``kernel_name``, allows specifying the name of the kernel
to be used for the execution. By default, the kernel name is obtained from the
notebook metadata. The traitlet ``kernel_name`` allows specifying a
user-defined kernel, overriding the value in the notebook metadata. A common
use case is that of a Python 2/3 library which includes documentation/testing
notebooks. These notebooks will specify either a python2 or python3 kernel in
their metadata (depending on the kernel used the last time the notebook was
saved). In reality, these notebooks will work on both Python 2 and Python 3,
and, for testing, it is important to be able to execute them programmatically
on both versions. Here the traitlet ``kernel_name`` helps simplify and
maintain consistency: we can just run a notebook twice, specifying first
"python2" and then "python3" as the kernel name.

Handling errors and exceptions
------------------------------

In the previous sections we saw how to save an executed notebook, assuming
there are no execution errors. But, what if there are errors?

Execution until first error
~~~~~~~~~~~~~~~~~~~~~~~~~~~
An error during the notebook execution, by default, will stop the execution
and raise a ``CellExecutionError``. Conveniently, the source cell causing
the error and the original error name and message are also printed.
After an error, we can still save the notebook as before::

    nbformat.write(nb, 'executed_notebook.ipynb')

The saved notebook contains the output up until the failing cell,
and includes a full stack-trace and error (which can help debugging).

Handling errors
~~~~~~~~~~~~~~~
A useful pattern to execute notebooks while handling errors is the following::

    from nbclient.exceptions import CellExecutionError

    try:
        client.execute()
    except CellExecutionError:
        msg = 'Error executing the notebook "%s".\n\n' % notebook_filename
        msg += 'See notebook "%s" for the traceback.' % notebook_filename_out
        print(msg)
        raise
    finally:
        nbformat.write(nb, notebook_filename_out)

This will save the executed notebook regardless of execution errors.
In case of errors, however, an additional message is printed and the
``CellExecutionError`` is raised. The message directs the user to
the saved notebook for further inspection.

Execute and save all errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~
As a last scenario, it is sometimes useful to execute notebooks which raise
exceptions, for example to show an error condition. In this case, instead of
stopping the execution on the first error, we can keep executing the notebook
using the traitlet ``allow_errors`` (default is False). With
``allow_errors=True``, the notebook is executed until the end, regardless of
any error encountered during the execution. The output notebook, will contain
the stack-traces and error messages for **all** the cells raising exceptions.

Widget state
------------

If your notebook contains any
`Jupyter Widgets <https://github.com/jupyter-widgets/ipywidgets/>`_,
the state of all the widgets can be stored in the notebook's metadata.
This allows rendering of the live widgets on for instance nbviewer, or when
converting to html.

We can tell nbclient to not store the state using the `store_widget_state`
argument::

    client = NotebookClient(nb, store_widget_state=False)

This widget rendering is not performed against a browser during execution, so
only widget default states or states manipulated via user code will be
calculated during execution. ``%%javascript`` cells will execute upon notebook
rendering, enabling complex interactions to function as expected when viewed by
a UI.

If you can't view widget results after execution, you may need to select
:menuselection:`Trust Notebook` under the :menuselection:`File` menu.

Using a command-line interface
------------------------------

This section will illustrate how to run notebooks from your terminal. It supports the most basic use case. For more sophisticated execution options, consider the `papermill <https://pypi.org/project/papermill/>`_ library.

This library's command line tool is available by running `jupyter execute`. It expects notebooks as input arguments and accepts optional flags to modify the default behavior.

Running a notebook is this easy.::

    jupyter execute notebook.ipynb

You can pass more than one notebook as well.::

    jupyter execute notebook.ipynb notebook2.ipynb

By default, notebook errors will be raised and printed into the terminal. You can suppress them by passing the ``--allow-errors`` flag.::

    jupyter execute notebook.ipynb --allow-errors

Other options allow you to modify the timeout length and dictate the kernel in use. A full set of options is available via the help command.::

    jupyter execute --help

    An application used to execute notebook files (*.ipynb)

    Options
    =======
    The options below are convenience aliases to configurable class-options,
    as listed in the "Equivalent to" description-line of the aliases.
    To see all configurable class-options for some <cmd>, use:
        <cmd> --help-all

    --allow-errors
        Errors are ignored and execution is continued until the end of the notebook.
        Equivalent to: [--NbClientApp.allow_errors=True]
    --timeout=<Int>
        The time to wait (in seconds) for output from executions. If a cell
        execution takes longer, a TimeoutError is raised. ``-1`` will disable the
        timeout.
        Default: None
        Equivalent to: [--NbClientApp.timeout]
    --startup_timeout=<Int>
        The time to wait (in seconds) for the kernel to start. If kernel startup
        takes longer, a RuntimeError is raised.
        Default: 60
        Equivalent to: [--NbClientApp.startup_timeout]
    --kernel_name=<Unicode>
        Name of kernel to use to execute the cells. If not set, use the kernel_spec
        embedded in the notebook.
        Default: ''
        Equivalent to: [--NbClientApp.kernel_name]

    To see all available configurables, use `--help-all`.
