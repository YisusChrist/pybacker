"""Command-line interface for the project."""

from argparse import ArgumentParser, Namespace
from pathlib import Path

import requests
from rich import print
from rich_argparse_plus import RichHelpFormatterPlus

from . import GITHUB
from . import __desc__ as DESC
from . import __version__ as VERSION
from .consts import MAX_TIMEOUT, NAME


def get_parsed_args() -> Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        The parsed arguments as a Namespace object.
    """
    parser = ArgumentParser(
        description=DESC,  # Program description
        formatter_class=RichHelpFormatterPlus,  # Disable line wrapping
        allow_abbrev=False,  # Disable abbreviations
        add_help=False,  # Disable default help
    )

    g_main = parser.add_argument_group("Main Options")
    # Source path argument
    g_main.add_argument(
        "-p",
        "--path",
        dest="path",
        metavar="PATH",
        default=Path.cwd(),
        help="The path that will store the directory of the backup.",
    )
    g_main.add_argument(
        "-f",
        "--files",
        dest="files",
        metavar="FILES",
        default="",
        help="The files to backup. Default is empty. [red]NOT IMPLEMENTED YET[/]",
    )
    g_main.add_argument(
        "-e",
        "--exclude",
        dest="exclude",
        metavar="EXCLUDE",
        default="",
        help="The files to exclude from the backup. Default is empty. [red]NOT IMPLEMENTED YET[/]",
    )
    g_main.add_argument(
        "-o",
        "--output",
        dest="output",
        metavar="OUTPUT",
        default="",
        help="The output directory for the backup. Default is [i]backup_<timestamp>.[/]",
    )

    g_misc = parser.add_argument_group("Miscellaneous Options")
    # Help
    g_misc.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit."
    )
    # Version
    g_misc.add_argument(
        "-V",
        "--version",
        action="version",
        help="Show version number and exit.",
        version=f"[argparse.prog]{NAME}[/] version [i]{VERSION}[/]",
    )

    return parser.parse_args()


def check_updates() -> None:
    """
    Check if there is a newer version of the script available in the GitHub repository.
    """
    project = GITHUB.split("https://github.com/")[1]
    repo_url = f"https://api.github.com/repos/{project}/releases/latest"

    try:
        response = requests.get(repo_url, timeout=MAX_TIMEOUT)
        response.raise_for_status()

        latest_version = response.json()["tag_name"]
        if latest_version != VERSION:
            print(
                f"\n[yellow]Newer version of the script available: {latest_version}.\n"
                "Please consider updating your version.[/yellow]"
            )

    except requests.exceptions.RequestException as e:
        print(f"[red]ERROR[/]: Could not check for updates: {e}")
