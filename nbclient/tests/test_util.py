import asyncio
import unittest.mock
from unittest.mock import MagicMock

import psutil
import pytest
import tornado

from nbclient.util import just_run, run_hook, run_sync


@run_sync
async def some_async_function():
    await asyncio.sleep(0.01)
    return 42


def test_nested_asyncio_with_existing_ioloop():
    async def _test():
        assert some_async_function() == 42
        return asyncio.get_running_loop()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        event_loop = loop.run_until_complete(_test())
        assert event_loop is loop
    finally:
        asyncio._set_running_loop(None)  # it seems nest_asyncio doesn't reset this


def test_nested_asyncio_with_no_ioloop():
    asyncio.set_event_loop(None)
    try:
        assert some_async_function() == 42
    finally:
        asyncio._set_running_loop(None)  # it seems nest_asyncio doesn't reset this


def test_nested_asyncio_with_tornado():
    # This tests if tornado accepts the pure-Python Futures, see
    # https://github.com/tornadoweb/tornado/issues/2753
    # https://github.com/erdewit/nest_asyncio/issues/23
    asyncio.set_event_loop(asyncio.new_event_loop())
    ioloop = tornado.ioloop.IOLoop.current()

    async def some_async_function():
        future: asyncio.Future = asyncio.ensure_future(asyncio.sleep(0.1))
        # this future is a different future after nested-asyncio has patched
        # the asyncio module, check if tornado likes it:
        ioloop.add_future(future, lambda f: f.result())  # type:ignore
        await future
        return 42

    def some_sync_function():
        return run_sync(some_async_function)()

    async def run():
        # calling some_async_function directly should work
        assert await some_async_function() == 42
        # but via a sync function (using nested-asyncio) can lead to issues:
        # https://github.com/tornadoweb/tornado/issues/2753
        assert some_sync_function() == 42

    ioloop.run_sync(run)


@pytest.mark.asyncio
async def test_run_hook_sync():
    some_sync_function = MagicMock()
    await run_hook(some_sync_function)
    assert some_sync_function.call_count == 1


@pytest.mark.asyncio
async def test_run_hook_async():
    hook = MagicMock(return_value=some_async_function())
    await run_hook(hook)
    assert hook.call_count == 1


def test_just_run_doesnt_leak_fds():
    proc = psutil.Process()

    async def async_sleep():
        await asyncio.sleep(0.01)

    # Warmup, just to make sure we're not failing on some initial fds being opened for the first time.
    for _ in range(10):
        just_run(async_sleep())
    fds_count = proc.num_fds()

    diff = []
    for _ in range(10):
        just_run(async_sleep())
        diff.append(proc.num_fds() - fds_count)
    assert diff == [0] * 10


def test_just_run_clears_new_loop():
    async def async_sleep():
        await asyncio.sleep(0.1)

    loop = asyncio.new_event_loop()
    loop.stop = MagicMock(wraps=loop.stop)
    loop.close = MagicMock(wraps=loop.close)

    with unittest.mock.patch.object(asyncio, "new_event_loop", return_value=loop):
        just_run(async_sleep())

    loop.stop.assert_called_once
    loop.close.assert_called_once
