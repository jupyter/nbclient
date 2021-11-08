# Changelog

## 0.5.5

- Added CLI to README [#170](https://github.com/jupyter/nbclient/pull/170) ([@palewire](https://github.com/palewire))
- Add "jupyter execute" command-line interface [#165](https://github.com/jupyter/nbclient/pull/165) ([@palewire](https://github.com/palewire))
- Fix: updating buffers overwrote previous buffers [#169](https://github.com/jupyter/nbclient/pull/169) ([@maartenbreddels](https://github.com/maartenbreddels))
- Fix tests for ipykernel without debugpy [#166](https://github.com/jupyter/nbclient/pull/166) ([@frenzymadness](https://github.com/frenzymadness))
- gitignore Pipfile [#164](https://github.com/jupyter/nbclient/pull/164) ([@palewire](https://github.com/palewire))
- Fixed CONTRIBUTING.md link [#163](https://github.com/jupyter/nbclient/pull/163) ([@palewire](https://github.com/palewire))
- Fix typo [#162](https://github.com/jupyter/nbclient/pull/162) ([@The-Compiler](https://github.com/The-Compiler))
- Move format & lint to pre-commit [#161](https://github.com/jupyter/nbclient/pull/161) ([@chrisjsewell](https://github.com/chrisjsewell))
- Add `skip-execution` cell tag functionality [#151](https://github.com/jupyter/nbclient/pull/151) ([@chrisjsewell](https://github.com/chrisjsewell))

## 0.5.4

- Replace `km.cleanup` with `km.cleanup_resources` [#152](https://github.com/jupyter/nbclient/pull/152) ([@davidbrochart](https://github.com/davidbrochart))
- Use async generator backport only on old python [#154](https://github.com/jupyter/nbclient/pull/154) ([@mkoeppe](https://github.com/mkoeppe))
- Support parsing of IPython dev version [#150](https://github.com/jupyter/nbclient/pull/150) ([@cphyc](https://github.com/cphyc))
- Set `IPYKERNEL_CELL_NAME = <IPY-INPUT>` [#147](https://github.com/jupyter/nbclient/pull/147) ([@davidbrochart](https://github.com/davidbrochart))
- Print useful error message on exception [#142](https://github.com/jupyter/nbclient/pull/142) ([@certik](https://github.com/certik))

## 0.5.3

- Fix ipykernel's `stop_on_error` value to take into account `raises-exception` tag and `force_raise_errors` [#137](https://github.com/jupyter/nbclient/pull/137)

## 0.5.2

- Set minimum python version supported to 3.6.1 to avoid 3.6.0 issues
- CellExecutionError is now unpickleable
- Added testing for python 3.9
- Changed travis tests to github actions
- Documentation referencing an old model instead of NotebookClient was fixed
- `allow_error_names` option was added for a more specific scope of `allow_errors` to be applied

## 0.5.1

- Update kernel client class JIT if it's the synchronous version
- Several documentation fixes / improvements

## 0.5.0

- Move `language_info` retrieval before cell execution [#102](https://github.com/jupyter/nbclient/pull/102)
- HistoryManager setting for ipython kernels no longer applies twice (fix for 5.0 trailets release)
- Improved error handling around language_info missing
- `(async_)start_new_kernel_client` is now split into `(async_)start_new_kernel` and `(async_)start_new_kernel_client`

## 0.4.2 - 0.4.3

These patch releases were removed due to backwards incompatible changes that should have been a minor release.
If you were using these versions for the couple days they were up, move to 0.5.0 and you shouldn't have any issues.

## 0.4.1

- Python type hinting added to most interfaces! [#83](https://github.com/jupyter/nbclient/pull/83)
- Several documentation fixes and improvements were made [#86](https://github.com/jupyter/nbclient/pull/86)
- An asynchronous heart beat check was added to correctly raise a DeadKernelError when kernels die unexpectantly [#90](https://github.com/jupyter/nbclient/pull/90)

## 0.4.0

### Major Changes

- Use KernelManager's graceful shutdown rather than KILLing kernels [#64](https://github.com/jupyter/nbclient/pull/64)
- Mimic an Output widget at the frontend so that the Output widget behaves correctly [#68](https://github.com/jupyter/nbclient/pull/68)
- Nested asyncio is automatic, and works with Tornado [#71](https://github.com/jupyter/nbclient/pull/71)
- `async_execute` now has a `reset_kc` argument to control if the client is reset upon execution request [#53](https://github.com/jupyter/nbclient/pull/53)

### Fixes

- Fix `OSError: [WinError 6] The handle is invalid` for windows/python<3.7 [#77](https://github.com/jupyter/nbclient/pull/77)
- Async wapper Exceptions no longer loose thier caused exception information [#65](https://github.com/jupyter/nbclient/pull/65)
- `extra_arguments` are now configurable by config settings [#66](https://github.com/jupyter/nbclient/pull/66)

### Operational

- Cross-OS testing now run on PRs via Github Actions [#63](https://github.com/jupyter/nbclient/pull/63)

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
