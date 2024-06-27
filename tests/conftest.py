"""Set up the test environment."""

from collections.abc import Generator

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem
from pyfakefs.fake_filesystem_unittest import Patcher
from pytest_mock import MockerFixture

FAKE_LOCKFILE = """
[[package]]
name = "package-a"
version = "1.0.0"
description = "A sample package A"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "package-b"
version = "2.0.0"
description = "A sample package B"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "package-c"
version = "3.0.0"
description = "A sample package C"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "package-d"
version = "4.0.0"
description = "A sample package D"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "package-e"
version = "5.0.0"
description = "A sample package E"
category = "main"
optional = false
python-versions = "*"

[metadata]
lock-version = "1.1"
python-versions = "*"
content-hash = "sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"

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
def get_fs(fs: FakeFilesystem) -> Generator[FakeFilesystem, None, None]:
    """Fixture to use pyfakefs with pytest."""
    with Patcher():
        fs.create_dir("/mocked/path")
        yield fs


@pytest.fixture()
def mock_data_dir(mocker) -> MockerFixture:
    """Fixture to mock platformdirs.user_data_dir and set return value."""
    mock = mocker.patch("platformdirs.user_data_dir")
    mock.return_value = "/mocked/path"
    return mock
