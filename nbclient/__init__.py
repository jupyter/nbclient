import asyncio
import sys

from ._version import __version__  # noqa
from ._version import version_info  # noqa
from .client import NotebookClient, execute  # noqa: F401


def _cleanup() -> None:
    pass


if sys.platform.startswith('win') and sys.version_info >= (3, 8) and sys.version_info < (3, 10):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
