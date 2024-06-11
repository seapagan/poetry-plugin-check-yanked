"""Define the 'check-yanked' command."""

from pathlib import Path

import requests
import rtoml
from poetry.console.commands.command import Command

from poetry_plugin_check_yanked import status


class CheckYankedCommand(Command):
    """Define the 'check-yanked' command."""

    name = "check-yanked"
    description = "Check for yanked packages in the poetry.lock file"
    help = (
        "The <c1>check-yanked</> Command checks through the "
        "<fg=green>poetry.lock</> file, and reports any packages that have "
        "been yanked fom PyPI along with the version number and reason."
    )

    def handle(self) -> int:
        """Handle the command."""
        lockfile_path = Path("poetry.lock")
        yanked_packages = self.get_yanked_packages(lockfile_path)

        if yanked_packages:
            self.line("\n<fg=red>Yanked packages found:</>\n")
            for name, version, reason in yanked_packages:
                self.line_error(
                    f'-> "<fg=red>{name}</>" version {version} '
                    f"(<fg=yellow>{reason}</>)"
                )
            return 1

        self.line("\n<fg=green>No yanked packages found.")
        return 0

    def get_yanked_packages(
        self, lockfile_path: Path
    ) -> list[tuple[str, str, str]]:
        """Return a list of the yanked packages in the lockfile.

        Returns a list of tuples, where each tuple contains the name, version
        and reason. If no yanked packages are found, an empty list is returned.
        """
        with lockfile_path.open() as file:
            lock_data = rtoml.load(file)

        yanked_packages = []
        timeout_seconds = 10

        self.info(
            f"\nChecking <fg=green>{len(lock_data['package'])}</> "
            "packages in poetry.lock"
        )

        for package in lock_data["package"]:
            name = package["name"]
            version = package["version"]

            try:
                response = requests.get(
                    f"https://pypi.org/pypi/{name}/{version}/json",
                    timeout=timeout_seconds,
                )

                if response.status_code == status.HTTP_200_OK:
                    package_info = response.json()
                    yanked = package_info["info"].get("yanked", False)

                    if yanked:
                        yanked_reason = package_info["info"].get(
                            "yanked_reason"
                        )
                        yanked_packages.append((name, version, yanked_reason))
                        if self.io.is_verbose():
                            self.line(
                                f"Checking package: {name} - <fg=red>Yanked</> "
                                f'(<fg=yellow>'
                                f'{package_info["info"]["yanked_reason"]}</>)'
                            )
                    elif self.io.is_verbose():
                        self.line(f"Checking package: {name} - <fg=green>OK</>")
                else:
                    self.line_error(
                        f"Error fetching data for {name}=={version}: "
                        f"HTTP {response.status_code}"
                    )

            except requests.Timeout:
                self.line_error(
                    f"Request for {name}=={version} timed out "
                    "after {timeout_seconds} seconds"
                )
            except requests.RequestException as e:
                self.line_error(f"Request for {name}=={version} failed: {e}")

        return yanked_packages
