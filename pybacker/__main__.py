"""Backup files and directories from a list of files"""
import sys
import time
from pathlib import Path
from shutil import copytree, rmtree
from tkinter import Tk, filedialog

from rich import print
from rich.traceback import install

from .cli import check_updates, get_parsed_args
from .consts import DEBUG, EXIT_FAILURE, EXIT_SUCCESS


def check_dir_list(dirs: list) -> bool:
    """
    Check if a list of directories exist

    Args:
        dirs (list): List of directories to check

    Returns:
        bool: True if all directories exist, False otherwise
    """
    for dir in dirs:
        if not Path(dir).exists():
            print(f"   Directory '{dir}' does not exist")
            return False

    return True


def create_backup_dir(base_path) -> Path:
    if not Path(base_path).exists():
        print(f"   [red]ERROR[/]: Base path '{base_path}' does not exist")
        sys.exit(EXIT_FAILURE)

    backup_dir = Path(base_path) / f"backup_{round(time.time())}"

    try:
        backup_dir.mkdir()
    except FileExistsError:
        print(
            f"   [yellow]WARNING[/]: Backup directory '{backup_dir}' "
            "already exists. Aborting."
        )
        sys.exit(EXIT_FAILURE)
    except Exception as e:
        print(f"   [red]ERROR[/]: Can not create backup directory: {e}")
        sys.exit(EXIT_FAILURE)

    return backup_dir


def check_directories(backup_dir, files):
    if not check_dir_list(files):
        print("   [red]ERROR[/]: Some directories do not exist")
        cleanup_and_exit(EXIT_FAILURE, backup_dir)

    print("   All directories exist [green]OK[/]")


def create_empty(backup_dir: Path, files: list) -> None:
    """
    Create empty containers for the files to be backed up

    Args:
        backup_dir (Path): Directory where the backup will be stored
        files (list): List of files to create empty containers for

    Notes:
        This function is used to create empty directories and files
        so that the files can be copied to the backup directory
        without having to create the directories and files manually
    """
    for file in files:
        try:
            file_path = Path(*Path(file).parent.parts[1:])
        except IndexError:
            file_path = Path("")

        # Use joinpath for proper concatenation
        file_path = backup_dir.joinpath(file_path)
        print(f"   Creating empty container for '{file}' with path '{file_path}'")

        # Make the directory if it doesn't exist
        file_path.mkdir(parents=True, exist_ok=True)


def get_file_list(backup_dir: Path) -> list:
    """
    Get the list of files to be backed up from a file

    Returns:
        list: List of files to be backed up
    """
    print("   Select the file with the list to be backed up")
    # Create a Tk root window
    root = Tk()
    # Hide the main window
    root.withdraw()
    # Ask the user to select a file
    file_path = filedialog.askopenfilename()
    if not file_path:
        print("   No file selected.")
        cleanup_and_exit(EXIT_FAILURE, backup_dir)

    file_name = Path(file_path).name
    print(f"   Reading file '{file_name}'...")

    with open(file_path, "r", encoding="utf-8") as f:
        files = [
            line.strip()
            for line in f.readlines()
            if not line.startswith("#") and line.strip()
        ]

    return files


def copy_files(backup_dir: Path, files: list) -> None:
    for file in files:
        source_path = Path(file)
        dest_path = backup_dir.joinpath(Path(*Path(file).parts[1:]))

        try:
            copytree(source_path, dest_path, dirs_exist_ok=True)
        except Exception as e:
            print(f"   Error backing up file '{source_path}': {e}")
            cleanup_and_exit(EXIT_FAILURE, backup_dir)


def check_backup_directory(backup_dir, files):
    source_files = [Path(file) for file in files]
    bak_files = [backup_dir.joinpath(Path(*file.parts[1:])) for file in source_files]

    # Check if source folders exist in backup directory
    if not check_dir_list([str(bak_file) for bak_file in bak_files]):
        print("   [red]ERROR[/]: Some directories could not be backed up")
        cleanup_and_exit(EXIT_FAILURE, backup_dir)

    # Check if the number of files in the source directory matches the backup directory
    for source_file, bak_file in zip(source_files, bak_files):
        source_file_count = sum(1 for _ in source_file.rglob("*") if _.is_file())
        bak_file_count = sum(1 for _ in bak_file.rglob("*") if _.is_file())

        if source_file_count != bak_file_count:
            print(f"   [red]ERROR[/]: File count mismatch for '{source_file}'.")
            cleanup_and_exit(EXIT_FAILURE, backup_dir)

        source_dir_count = sum(1 for _ in source_file.rglob("*") if _.is_dir())
        bak_dir_count = sum(1 for _ in bak_file.rglob("*") if _.is_dir())

        if source_dir_count != bak_dir_count:
            print(f"   [red]ERROR[/]: Folder count mismatch for '{source_file}'.")
            cleanup_and_exit(EXIT_FAILURE, backup_dir)

    print("   Backup completed successfully!")


def cleanup_and_exit(exit_code: int, backup_dir: Path) -> None:
    try:
        print(f"   Cleaning up backup directory '{backup_dir}'...")
        rmtree(backup_dir)
    except Exception as e:
        print(
            f"   [red]ERROR[/]: Could not clean up "
            f"backup directory '{backup_dir}': {e}"
        )

    sys.exit(exit_code)


def main():
    args = get_parsed_args()
    
    check_updates()

    base_path = args.path if args.path else Path.cwd()

    backup_dir = create_backup_dir(base_path)
    print(f"1. Creating backup directory '{backup_dir}'...")

    print("2. Getting list of files to be backed up...")
    files = get_file_list(backup_dir)

    print("3. Checking directories...")
    check_directories(backup_dir, files)

    print(f"4. Creating empty containers in '{backup_dir}'...")
    # TODO: This seems to be unnecessary when using copytree with dirs_exist_ok=True
    # Still need to check if this is the case in other platforms (Linux, MacOS)
    create_empty(backup_dir, files)

    print("5. Backing up files...")
    copy_files(backup_dir, files)

    print("6. Checking backup directory...")
    check_backup_directory(backup_dir, files)

    sys.exit(EXIT_SUCCESS)


if __name__ == "__main__":
    # Enable rich error formatting in debug mode
    install(show_locals=DEBUG)
    main()
