"""Implement a Poetry plugin.

This plugin will check through your 'poetry.lock' and ensure that there are no
'Yanked' packages in there.
"""

from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_yanked_check.command import YankedCheckerCommand


def factory() -> YankedCheckerCommand:
    """Define the factory for the 'check-yanked' command."""
    return YankedCheckerCommand()


class YankedCheckerPlugin(ApplicationPlugin):
    """Define the 'yanked-checker' plugin."""

    def activate(self, application: Application) -> None:
        """Called after the plugin is loaded."""
        application.command_loader.register_factory("check-yanked", factory)


if __name__ == "__main__":
    checker = YankedCheckerCommand()
    checker.handle()
