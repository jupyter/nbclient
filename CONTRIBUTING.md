# Contributing

We follow the [Jupyter Contribution Workflow](https://jupyter.readthedocs.io/en/latest/contributing/content-contributor.html) and the [IPython Contributing Guide](https://github.com/ipython/ipython/blob/master/CONTRIBUTING.md).

## Code formatting

Use the [pre-commit](https://pre-commit.com/) tool to format and lint the codebase:

```console
# to apply to only staged files
$ pre-commit run
# to run against all files
$ pre-commit run --all-files
# to install so that it is run before commits
$ pre-commit install
```

## Testing

In your environment `pip install -e '.[test]'` will be needed to be able to
run all of the tests.

The recommended way to do this is using [tox](https://tox.readthedocs.io/en/latest/):

```console
# to list all environments
$ tox -av
# to run all tests for a specific environment
$ tox -e py38
```

## Documentation

NbClient needs some PRs to copy over documentation!

## Releasing

If you are going to release a version of `nbclient` you should also be capable
of testing it and building the docs.

Please follow the instructions in [Testing](#testing) and [Documentation](#documentation) if
you are unfamiliar with how to do so.

The rest of the release process can be found in [these release instructions](./RELEASING.md).
