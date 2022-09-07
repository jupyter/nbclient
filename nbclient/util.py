"""General utility methods"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import asyncio
import inspect
from typing import Any, Awaitable, Callable, Coroutine, Optional, TypeVar, Union

T = TypeVar("T")


def just_run(coro: Coroutine[Any, Any, T]) -> T:
    """Make the coroutine run, even if there is already a running event loop"""
    try:
        loop_prev = asyncio.get_running_loop()
    except RuntimeError:
        loop_prev = None
    loop = loop_prev or asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # private API, but present from CPython 3.3ish-3.10+
    asyncio.events._set_running_loop(None)
    res: T = asyncio.run(coro)
    if loop_prev:
        asyncio.set_event_loop(loop_prev)
        asyncio.events._set_running_loop(loop_prev)
    return res


def run_sync(coro: Callable[..., Coroutine[Any, Any, T]]) -> Callable[..., T]:
    """Runs a coroutine and blocks until it has executed.

    An event loop is created if no one already exists. If an event loop is
    already running, this event loop execution is nested into the already
    running one if `nest_asyncio` is set to True.

    Parameters
    ----------
    coro : coroutine
        The coroutine to be executed.

    Returns
    -------
    result :
        Whatever the coroutine returns.
    """

    def wrapped(*args, **kwargs):
        return just_run(coro(*args, **kwargs))

    wrapped.__doc__ = coro.__doc__
    return wrapped


async def ensure_async(obj: Union[Awaitable, Any]) -> Any:
    """Convert a non-awaitable object to a coroutine if needed,
    and await it if it was not already awaited.
    """
    if inspect.isawaitable(obj):
        try:
            result = await obj
        except RuntimeError as e:
            if str(e) == 'cannot reuse already awaited coroutine':
                # obj is already the coroutine's result
                return obj
            raise
        return result
    # obj doesn't need to be awaited
    return obj


async def run_hook(hook: Optional[Callable], **kwargs: Any) -> None:
    if hook is None:
        return
    res = hook(**kwargs)
    if inspect.isawaitable(res):
        await res
