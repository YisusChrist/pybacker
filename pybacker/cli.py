"""Command-line interface for the project."""

from argparse import Namespace
from pathlib import Path

from core_helpers.cli import ArgparseColorThemes, setup_parser

from .consts import PACKAGE
from .consts import __desc__ as DESC
from .consts import __version__ as VERSION


def get_parsed_args() -> Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        The parsed arguments as a Namespace object.
    """
    parser, g_main = setup_parser(
        PACKAGE,
        DESC,
        VERSION,
        ArgparseColorThemes.DEFAULT,
    )

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

    return parser.parse_args()
