"""General utility methods"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import asyncio
import inspect


def run_sync(coro):
    """Runs a coroutine and blocks until it has executed.

    An event loop is created if no one already exists. If an event loop is
    already running, this event loop execution is nested into the already
    running one.

    Parameters
    ----------
    coro : coroutine
        The coroutine to be executed.

    Returns
    -------
    result :
        Whatever the coroutine returns.
    """
    def wrapped(self, *args, **kwargs):
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        try:
            c = coro(self, *args, **kwargs)
            result = loop.run_until_complete(c)
        except RuntimeError as e:
            if str(e) == 'This event loop is already running':
                import nest_asyncio
                nest_asyncio.apply(loop)
                result = loop.run_until_complete(c)
            else:
                raise
        return result
    wrapped.__doc__ = coro.__doc__
    return wrapped


async def ensure_async(obj):
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
