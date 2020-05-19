# Changelog

## 0.3.1

### Fixes

- Check that a kernel manager exists before cleaning up the kernel [#61](https://github.com/jupyter/nbclient/pull/61)
- Force client class to be async when kernel manager is MultiKernelManager [#55](https://github.com/jupyter/nbclient/pull/55)
- Replace pip install with conda install in Binder [#54](https://github.com/jupyter/nbclient/pull/54)

## 0.3.0

### Major Changes

- The `(async_)start_new_kernel_client` method now supports starting a new client when its kernel manager (`self.km`) is a `MultiKernelManager`. The method now returns the kernel id in addition to the kernel client. If the kernel manager was a `KernelManager`, the returned kernel id is `None`. [#51](https://github.com/jupyter/nbclient/pull/51)
- Added sphinx-book-theme for documentation. Added a CircleCI job to let us preview the built documentation in a PR. [#50](https://github.com/jupyter/nbclient/pull/50)
- Added `reset_kc` option to `reset_execution_trackers`, so that the kernel client can be reset and a new one created in calls to `(async_)execute` [#44](https://github.com/jupyter/nbclient/pull/44)

### Docs

- Fixed documentation [#46](https://github.com/jupyter/nbclient/pull/46) [#47](https://github.com/jupyter/nbclient/pull/47)
- Added documentation status badge to the README
- Removed conda from documentation build

## 0.2.0

### Major Changes

- Async support is now available on the client. Methods that support async have an `async_` prefix and can be awaited [#10](https://github.com/jupyter/nbclient/pull/10) [#35](https://github.com/jupyter/nbclient/pull/35) [#37](https://github.com/jupyter/nbclient/pull/37) [#38](https://github.com/jupyter/nbclient/pull/38)
- Dropped support for Python 3.5 due to async compatability issues [#34](https://github.com/jupyter/nbclient/pull/34)
- Notebook documents now include the [new kernel timing fields](https://github.com/jupyter/nbformat/pull/144) [#32](https://github.com/jupyter/nbclient/pull/32)

### Fixes

- Memory and process leaks from nbclient should now be fixed [#34](https://github.com/jupyter/nbclient/pull/34)
- Notebook execution exceptions now include error information in addition to the message [#41](https://github.com/jupyter/nbclient/pull/41)

### Docs

- Added [binder examples](https://mybinder.org/v2/gh/jupyter/nbclient/master?filepath=binder%2Frun_nbclient.ipynb) / tests [#7](https://github.com/jupyter/nbclient/pull/7)
- Added changelog to docs [#22](https://github.com/jupyter/nbclient/pull/22)
- Doc typo fixes [#27](https://github.com/jupyter/nbclient/pull/27) [#30](https://github.com/jupyter/nbclient/pull/30)

## 0.1.0

- Initial release -- moved out of nbconvert 6.0.0-a0
