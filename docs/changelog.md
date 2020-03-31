# Changelog

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
