"""Define the 'check-yanked' command."""

from __future__ import annotations

import datetime
from pathlib import Path
from typing import Any

import pickledb
import platformdirs
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

    def __init__(self) -> None:
        """Initialize the command."""
        super().__init__()

        self._data_dir = Path(
            platformdirs.user_data_dir(appname="poetry-yanked-check")
        )
        self._data_dir.mkdir(parents=True, exist_ok=True)
        self.cache = pickledb.load(self._data_dir / "cache.db", False)
        self.yanked_packages: list[
            tuple[str, str, dict[str, str | bool | None]]
        ] = []
        self.timeout_seconds = 10

    def handle(self) -> int:
        """Handle the command."""
        lockfile_path = Path("poetry.lock")
        yanked_packages = self.get_yanked_packages(lockfile_path)

        if yanked_packages:
            self.line("\n<fg=red>Yanked packages found:</>\n")
            for name, version, status in yanked_packages:
                self.line_error(
                    f'-> "<fg=red>{name}</>" version {version} '
                    f'(<fg=yellow>{status["yanked_reason"]}</>)'
                )
            return 1

        self.line("\n<fg=green>No yanked packages found.")
        return 0

    def get_yanked_packages(
        self, lockfile_path: Path
    ) -> list[tuple[str, str, dict[str, Any]]]:
        """Return a list of the yanked packages in the lockfile.

        Returns a list of tuples, where each tuple contains the name, version
        and reason. If no yanked packages are found, an empty list is returned.
        """
        with lockfile_path.open() as file:
            lock_data = rtoml.load(file)

        self.info(
            f"\nChecking <fg=green>{len(lock_data['package'])}</> "
            "packages in poetry.lock"
        )

        for package in lock_data["package"]:
            version, status = self.check_package(package)
            if status["yanked"]:
                self.yanked_packages.append((package["name"], version, status))
                if self.io.is_verbose():
                    self.line(
                        f'Checking {package["name"]} - '
                        "<fg=red>Yanked</> (<fg=yellow>"
                        f'{status["yanked_reason"]}</>)'
                    )
            elif self.io.is_verbose():
                self.line(f'Checking {package["name"]} - <fg=green>OK</>')

        return self.yanked_packages

    def check_package(
        self, package: dict[str, Any]
    ) -> tuple[str, dict[str, Any]]:
        """Check the specified package for yanked status.

        If it exists in the cache, return the cached value. Otherwise, fetch
        the package info from PyPI and return the result.
        """
        package_name: str = package["name"]
        package_version: str = package["version"]

        if self.cache.exists(package_name):
            library_info = self.cache.get(package_name)
        else:
            library_info = {}

        if package_version in library_info:
            return (package_version, library_info[package_version])

        new_package = self.request_package(package_name, package_version)
        library_info[package_version] = new_package
        self.cache.set(package_name, library_info)
        self.cache.dump()

        return (package_version, new_package)

    def request_package(self, name: str, version: str) -> dict[str, Any]:
        """Request the package info from PyPI.

        Return the yanked status and reason, if available.
        """
        try:
            response = requests.get(
                f"https://pypi.org/pypi/{name}/{version}/json",
                timeout=self.timeout_seconds,
            )

            last_checked = self.get_timestamp()

            if response.status_code == status.HTTP_200_OK:
                package_info = response.json()
                yanked = package_info["info"].get("yanked", False)

                if yanked:
                    return {
                        "yanked": True,
                        "yanked_reason": package_info["info"].get(
                            "yanked_reason"
                        ),
                        "last_checked": last_checked,
                    }

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

        return {
            "yanked": False,
            "yanked_reason": None,
            "last_checked": last_checked,
        }

    def get_timestamp(self) -> int:
        """Return the current timestamp as a string.

        Removes any decimal places and microseconds.
        """
        return int(
            datetime.datetime.now(tz=datetime.timezone.utc)
            .replace(microsecond=0)
            .timestamp()
        )
