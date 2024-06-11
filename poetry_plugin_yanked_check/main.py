"""Implement a Poetry plugin.

This plugin will check through your 'poetry.lock' and ensure that there are no
'Yanked' packages in there.
"""

from pathlib import Path

import requests
import rtoml
from poetry.console.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_yanked_check.status import HTTP_200_OK


class YankedCheckerCommand(Command):
    """Define the 'check-yanked' command."""

    name = "check-yanked"
    description = "Check for yanked packages in the poetry.lock file"

    def handle(self) -> int:
        """Handle the command."""
        lockfile_path = Path("poetry.lock")
        yanked_packages = self.get_yanked_packages(lockfile_path)

        if yanked_packages:
            self.line("Yanked packages found:")
            for name, version in yanked_packages:
                self.line(f"{name}=={version}")
            return 0

        self.line("No yanked packages found.")
        return 1

    def get_yanked_packages(self, lockfile_path: Path) -> list[tuple[str, str]]:
        """Return a list of the yanked packages in the lockfile.

        Returns a list of tuples, where each tuple contains the name and
        version. If no yanked packages are found, an empty list is returned.
        """
        with lockfile_path.open() as file:
            lock_data = rtoml.load(file)

        yanked_packages = []
        timeout_seconds = 10

        for package in lock_data["package"]:
            name = package["name"]
            version = package["version"]

            try:
                response = requests.get(
                    f"https://pypi.org/pypi/{name}/{version}/json",
                    timeout=timeout_seconds,
                )

                if response.status_code == HTTP_200_OK:
                    package_info = response.json()
                    yanked = package_info["info"].get("yanked", False)

                    if yanked:
                        yanked_packages.append((name, version))
                else:
                    self.line(
                        f"Error fetching data for {name}=={version}: "
                        f"HTTP {response.status_code}"
                    )

            except requests.Timeout:
                self.line(
                    f"Request for {name}=={version} timed out "
                    "after {timeout_seconds} seconds"
                )
            except requests.RequestException as e:
                self.line(f"Request for {name}=={version} failed: {e}")

        return yanked_packages


def factory() -> YankedCheckerCommand:
    """Define the factory for the 'check-yanked' command."""
    return YankedCheckerCommand()


class YankedCheckerPlugin(ApplicationPlugin):
    """Define the 'yanked-checker' plugin."""

    def activate(self, application: ApplicationPlugin) -> None:
        """Called after the plugin is loaded."""
        application.command_loader.register_factory("check-yanked", factory)


if __name__ == "__main__":
    checker = YankedCheckerCommand()
    checker.handle()
