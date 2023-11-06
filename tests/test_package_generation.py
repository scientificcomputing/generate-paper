import pytest
from pathlib import Path
import sys
import subprocess as sp


@pytest.fixture
def python_venv(tmp_path) -> str:
    """Create a new python virtual environment
    and return the path to the python executable
    """
    python = sys.executable
    # Create virual environment
    sp.run([python, "-m", "venv", tmp_path.as_posix()])
    yield (tmp_path / "bin" / "python").as_posix()


def test_bake_project(cookies, python_venv):
    result = cookies.bake(extra_context={"repository_name": "my_paper"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "my_paper"
    assert result.project_path.is_dir()

    assert result.project.basename == "my_paper"
    assert result.project.isdir()

    # Try to install the the package and run the tests
    result.project.chdir()
    res_install = sp.run(
        [python_venv, "-m", "pip", "install", ".[docs]"], capture_output=True
    )
    assert res_install.returncode == 0, res_install.stderr

    res_build_docs = sp.run(
        [python_venv, "-m", "jupyter", "book", "build", "-W", "."],
        capture_output=True,
    )

    assert res_build_docs.returncode == 0, res_build_docs.stderr
