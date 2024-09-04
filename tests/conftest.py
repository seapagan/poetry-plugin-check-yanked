"""Set up the test environment."""

import pytest
from poetry_plugin_check_yanked.command import CheckYankedCommand
from pyfakefs.fake_filesystem import FakeFilesystem
from pytest_mock import MockerFixture

FAKE_LOCKFILE = """
[[package]]
name = "package-a"
version = "1.0.0"
description = "A sample package A"
optional = false
python-versions = "*"

[[package]]
name = "package-b"
version = "2.0.0"
description = "A sample package B"
optional = false
python-versions = "*"

[[package]]
name = "package-c"
version = "3.0.0"
description = "A sample package C"
optional = false
python-versions = "*"

[[package]]
name = "package-d"
version = "4.0.0"
description = "A sample package D"
optional = false
python-versions = "*"

[[package]]
name = "package-e"
version = "5.0.0"
description = "A sample package E"
optional = false
python-versions = "*"

[metadata]
lock-version = "2.0"
python-versions = "*"
content-hash = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"


"""  # noqa: E501

# define a fake response from the PyPI API without any yanked packages.
FAKE_GOOD_RESPONSE = {
    "package-a": {
        "info": {
            "name": "package-a",
            "version": "1.0.0",
            "yanked": False,
            "yanked_reason": None,
        }
    },
    "package-b": {
        "info": {
            "name": "package-b",
            "version": "2.0.0",
            "yanked": False,
            "yanked_reason": None,
        }
    },
    "package-c": {
        "info": {
            "name": "package-c",
            "version": "3.0.0",
            "yanked": False,
            "yanked_reason": None,
        }
    },
    "package-d": {
        "info": {
            "name": "package-d",
            "version": "4.0.0",
            "yanked": False,
            "yanked_reason": None,
        }
    },
    "package-e": {
        "info": {
            "name": "package-e",
            "version": "5.0.0",
            "yanked": False,
            "yanked_reason": None,
        }
    },
}

# define a fake response from the PyPI API with a yanked package.
FAKE_YANKED_RESPONSE = FAKE_GOOD_RESPONSE
FAKE_YANKED_RESPONSE["package-b"]["info"]["yanked"] = True
FAKE_YANKED_RESPONSE["package-b"]["info"]["yanked_reason"] = (
    "Yanked for testing"
)


@pytest.fixture()
def get_fs(fs: FakeFilesystem) -> FakeFilesystem:
    """Fixture to use pyfakefs with pytest."""
    fs.create_dir("/mocked/path")
    fs.create_file("./poetry.lock", contents=FAKE_LOCKFILE)
    return fs


@pytest.fixture()
def mock_data_dir(mocker: MockerFixture) -> MockerFixture:
    """Fixture to mock platformdirs.user_data_dir and set return value."""
    mock = mocker.patch("platformdirs.user_data_dir")
    mock.return_value = "/mocked/path"
    return mock


@pytest.fixture()
def yank_class(
    get_fs: FakeFilesystem, mock_data_dir: MockerFixture
) -> CheckYankedCommand:
    """Fixture to return the CheckYankedCommand class.

    It also applies the mock filesystem and data directory.
    """
    return CheckYankedCommand()
