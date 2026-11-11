import sys
from pathlib import Path
from subprocess import CalledProcessError, check_output
from unittest.mock import call, mock_open, patch

import pytest
from nbformat import v4, write

from nbclient.cli import NbClientApp

if sys.version_info >= (3, 13):
    PATH_OPEN_CALL_STEP = 4
else:
    PATH_OPEN_CALL_STEP = 3

current_dir = Path(__file__).parent.absolute()


@pytest.fixture()
def jupyterapp():
    with patch("nbclient.cli.JupyterApp.initialize") as mocked:
        yield mocked


@pytest.fixture()
def client():
    with patch("nbclient.cli.NotebookClient", autospec=True) as mocked:
        yield mocked


@pytest.fixture()
def writer():
    with patch("nbformat.write", autospec=True) as mocked:
        yield mocked


@pytest.fixture()
def reader():
    with patch("nbformat.read", autospec=True, return_value="nb") as mocked:
        yield mocked


@pytest.fixture()
def path_open():
    opener = mock_open()

    def mocked_open(self, *args, **kwargs):
        return opener(self, *args, **kwargs)

    with patch("nbclient.cli.Path.open", mocked_open):
        yield opener


@pytest.mark.parametrize(
    "input_names", [("Other Comms",), ("Other Comms.ipynb",), ("Other Comms", "HelloWorld.ipynb")]
)
@pytest.mark.parametrize("relative", [False, True])
@pytest.mark.parametrize("inplace", [False, True])
def test_mult(input_names, relative, inplace, jupyterapp, client, reader, writer, path_open):
    paths = [current_dir / "files" / name for name in input_names]
    if relative:
        paths = [p.relative_to(Path.cwd()) for p in paths]

    c = NbClientApp(notebooks=[str(p) for p in paths], kernel_name="python3", inplace=inplace)
    c.initialize()

    # add suffix if needed
    paths = [p.with_suffix(".ipynb") for p in paths]

    assert path_open.mock_calls[::PATH_OPEN_CALL_STEP] == [call(p, encoding="utf-8") for p in paths]
    assert reader.call_count == len(paths)
    # assert reader.mock_calls == [call(p, as_version=4) for p in paths]

    expected = []
    for p in paths:
        expected.extend(
            [
                call(
                    "nb",
                    timeout=c.timeout,
                    startup_timeout=c.startup_timeout,
                    skip_cells_with_tag=c.skip_cells_with_tag,
                    allow_errors=c.allow_errors,
                    kernel_name=c.kernel_name,
                    resources={"metadata": {"path": p.parent.absolute()}},
                ),
                call().execute(),
            ]
        )

    assert client.mock_calls == expected

    if inplace:
        assert writer.mock_calls == [call("nb", p) for p in paths]
    else:
        writer.assert_not_called()


@pytest.mark.parametrize(
    "input_names", [("Other Comms",), ("Other Comms.ipynb",), ("Other Comms", "HelloWorld.ipynb")]
)
@pytest.mark.parametrize("relative", [False, True])
@pytest.mark.parametrize("output_base", ["thing", "thing.ipynb", "{notebook_name}-new.ipynb"])
def test_output(input_names, relative, output_base, jupyterapp, client, reader, writer, path_open):
    paths = [current_dir / "files" / name for name in input_names]
    if relative:
        paths = [p.relative_to(Path.cwd()) for p in paths]

    c = NbClientApp(
        notebooks=[str(p) for p in paths], kernel_name="python3", output_base=output_base
    )

    if len(paths) != 1 and "{notebook_name}" not in output_base:
        with pytest.raises(ValueError) as e:
            c.initialize()
        assert "If passing multiple" in str(e.value)
        return

    c.initialize()

    # add suffix if needed
    paths = [p.with_suffix(".ipynb") for p in paths]

    assert path_open.mock_calls[::PATH_OPEN_CALL_STEP] == [call(p, encoding="utf-8") for p in paths]
    assert reader.call_count == len(paths)

    expected = []
    for p in paths:
        expected.extend(
            [
                call(
                    "nb",
                    timeout=c.timeout,
                    startup_timeout=c.startup_timeout,
                    skip_cells_with_tag=c.skip_cells_with_tag,
                    allow_errors=c.allow_errors,
                    kernel_name=c.kernel_name,
                    resources={"metadata": {"path": p.parent.absolute()}},
                ),
                call().execute(),
            ]
        )

    assert client.mock_calls == expected

    assert writer.mock_calls == [
        call(
            "nb",
            (p.parent / output_base.format(notebook_name=p.with_suffix("").name)).with_suffix(
                ".ipynb"
            ),
        )
        for p in paths
    ]


def test_bad_output_dir(jupyterapp, client, reader, writer, path_open):
    input_names = ["Other Comms"]
    output_base = "thing/thing"

    paths = [current_dir / "files" / name for name in input_names]

    c = NbClientApp(
        notebooks=[str(p) for p in paths], kernel_name="python3", output_base=output_base
    )

    with pytest.raises(ValueError) as e:
        c.initialize()

    assert "Cannot write to directory" in str(e.value)


def test_read_utf8_notebook(tmp_path, monkeypatch, client):
    source = "print('caf\u00e9, \u4e16\u754c')"
    notebook_path = tmp_path / "unicode.ipynb"
    write(v4.new_notebook(cells=[v4.new_code_cell(source)]), notebook_path)

    # Simulate a non-UTF-8 locale while still reading the actual notebook bytes.
    path_open = Path.open

    def open_with_locale_encoding(path, *args, **kwargs):
        if kwargs.get("encoding") is None:
            kwargs["encoding"] = "cp1252"
        return path_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", open_with_locale_encoding)

    NbClientApp().run_notebook(str(notebook_path))

    assert client.call_args.args[0].cells[0].source == source
    client.return_value.execute.assert_called_once_with()


# simple runner from command line
def test_cli_simple():
    path = current_dir / "files" / "Other Comms"

    with pytest.raises(CalledProcessError):
        check_output(["jupyter-execute", "--output", "thing/thing", str(path)])  # noqa: S603, S607


def test_no_notebooks(jupyterapp):
    c = NbClientApp(notebooks=[], kernel_name="python3")

    with pytest.raises(SystemExit):
        c.initialize()
