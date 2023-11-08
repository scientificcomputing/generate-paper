import pytest
import sys
import subprocess as sp

from contextlib import contextmanager
from pathlib import Path

import os


@contextmanager
def set_directory(path: Path):
    """Sets the cwd within the context

    Args:
        path (Path): The path to the cwd

    Yields:
        None
    """

    origin = Path().absolute()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(origin)


@pytest.fixture
def python_venv(tmp_path) -> str:
    """Create a new python virtual environment
    and return the path to the python executable
    """
    python = sys.executable
    # Create virual environment
    sp.run([python, "-m", "venv", tmp_path.as_posix()])
    yield (tmp_path / "bin" / "python").as_posix()


@pytest.mark.parametrize(
    "use_conda, require_fenics, require_fenicsx, use_docker, open_source_license",
    (
        ("y", "n", "n", "n", "CC-BY-4.0"),
        ("y", "y", "n", "n", "MIT"),
        ("y", "y", "y", "n", "GPL-3.0"),
        ("y", "y", "y", "y", "Other"),
    ),
)
def test_bake_project(
    cookies,
    python_venv,
    use_conda,
    require_fenics,
    require_fenicsx,
    use_docker,
    open_source_license,
):
    result = cookies.bake(
        extra_context={
            "repository_name": "my_paper",
            "use_pre_commit": "y",
            "use_conda": use_conda,
            "require_fenics": require_fenics,
            "require_fenicsx": require_fenicsx,
            "use_docker": use_docker,
            "open_source_license": open_source_license,
        },
    )

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "my_paper"

    assert result.project_path.is_dir()

    assert result.project.basename == "my_paper"
    assert result.project.isdir()

    # Try to install the the package and run the tests
    with set_directory(result.project):
        res_install = sp.run(
            [python_venv, "-m", "pip", "install", ".[docs,dev]"],
            capture_output=True,
        )
        assert res_install.returncode == 0, res_install.stderr

        # Run linter
        res_git_init = sp.run(["git", "init"])
        assert res_git_init.returncode == 0, res_git_init.stderr

        res_git_add = sp.run(["git", "add", "."])
        assert res_git_add.returncode == 0, res_git_add.stderr

        res_pre_commit = sp.run(
            [python_venv.replace("python", "pre-commit"), "run", "--all"],
            capture_output=True,
        )
        assert res_pre_commit.returncode == 0, res_pre_commit.stdout.decode()

        res_build_docs = sp.run(
            [python_venv, "-m", "jupyter", "book", "build", "-W", "."],
            capture_output=True,
        )

        assert res_build_docs.returncode == 0, res_build_docs.stderr
