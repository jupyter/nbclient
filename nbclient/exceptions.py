class CellTimeoutError(TimeoutError):
    """
    A custom exception to capture when a cell has timed out during execution.
    """

    @classmethod
    def error_from_timeout_and_cell(cls, msg, timeout, cell):
        if cell and cell.source:
            src_by_lines = cell.source.strip().split("\n")
            src = (
                cell.source
                if len(src_by_lines) < 11
                else "{}\n...\n{}".format(src_by_lines[:5], src_by_lines[-5:])
            )
        else:
            src = "Cell contents not found."
        return cls(timeout_err_msg.format(timeout=timeout, msg=msg, cell_contents=src))


class DeadKernelError(RuntimeError):
    pass


class CellExecutionComplete(Exception):
    """
    Used as a control signal for cell execution across execute_cell and
    process_message function calls. Raised when all execution requests
    are completed and no further messages are expected from the kernel
    over zeromq channels.
    """

    pass


class CellExecutionError(Exception):
    """
    Custom exception to propagate exceptions that are raised during
    notebook execution to the caller. This is mostly useful when
    using nbconvert as a library, since it allows to deal with
    failures gracefully.
    """

    def __init__(self, traceback):
        super(CellExecutionError, self).__init__(traceback)
        self.traceback = traceback

    def __str__(self):
        s = self.__unicode__()
        if not isinstance(s, str):
            s = s.encode('utf8', 'replace')
        return s

    def __unicode__(self):
        return self.traceback

    @classmethod
    def from_cell_and_msg(cls, cell, msg):
        """Instantiate from a code cell object and a message contents
        (message is either execute_reply or error)
        """
        tb = '\n'.join(msg.get('traceback', []))
        return cls(
            exec_err_msg.format(
                cell=cell,
                traceback=tb,
                ename=msg.get('ename', '<Error>'),
                evalue=msg.get('evalue', ''),
            )
        )


exec_err_msg = u"""\
An error occurred while executing the following cell:
------------------
{cell.source}
------------------

{traceback}
{ename}: {evalue}
"""


timeout_err_msg = u"""\
A cell timed out while it was being executed, after {timeout} seconds.
The message was: {msg}.
Here is a preview of the cell contents:
-------------------
{cell_contents}
-------------------
"""
