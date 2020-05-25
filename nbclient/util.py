"""General utility methods"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import concurrent.futures
import asyncio
import inspect


blocking_thread = None


def run_in_thread(coro, self, *args, **kwargs):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    result = loop.run_until_complete(coro(self, *args, **kwargs))
    return result


def run_sync(coro):
    """Runs a coroutine and blocks until it has executed.

    An event loop is created in a new thread, and the coroutine is executed in
    that thread until completion.

    Parameters
    ----------
    coro : coroutine
        The coroutine to be executed.

    Returns
    -------
    result :
        Whatever the coroutine returns.
    """
    # create a new thread only if it is required (no need for async execution)
    # and only once
    global blocking_thread
    if blocking_thread is None:
        blocking_thread = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    def wrapped(self, *args, **kwargs):
        result = blocking_thread.submit(run_in_thread, coro, self, *args, **kwargs).result()
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
