"""Test the plugin.py module."""

from poetry.console.application import Application
from poetry_plugin_check_yanked.command import CheckYankedCommand
from poetry_plugin_check_yanked.plugin import CheckYankedPlugin, factory


def test_factory_returns_check_yanked_command() -> None:
    """Ensure that the factory returns the 'CheckYankedCommand' class."""
    assert isinstance(factory(), CheckYankedCommand)


def test_register_factory_called_with_correct_parameters(mocker) -> None:
    """Ensure that the 'register_factory' method is called correctly."""
    application = mocker.Mock(spec=Application)
    plugin = CheckYankedPlugin()
    plugin.activate(application)

    application.command_loader.register_factory.assert_called_once_with(
        "check-yanked", factory
    )
