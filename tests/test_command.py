"""Tests for the command module."""

from pathlib import Path

from poetry_plugin_check_yanked.command import (
    DEFAULT_TIMEOUT,
    CheckYankedCommand,
)


def test_check_yanked_command_init(get_fs, mocker, mock_data_dir) -> None:
    """Test the initialization of the CheckYankedCommand class."""
    mock_pickledb_load = mocker.patch("pickledb.load")
    mock_pickledb_load.return_value = mocker.Mock()

    command = CheckYankedCommand()

    mock_data_dir.assert_called_once_with(appname="poetry-yanked-check")
    assert (
        Path("/mocked/path").exists()
    )  # This checks if the directory was "created" in the fake file system
    mock_pickledb_load.assert_called_once_with(
        Path("/mocked/path") / "cache.db", False
    )

    assert command.cache is not None
    assert command.yanked_packages == []
    assert command.timeout_seconds == DEFAULT_TIMEOUT
