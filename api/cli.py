"""Module cli for argparse command line functions."""
# standard library imports
import argparse
import sys

# my own library imports
from .api import download_file, decompress_file, parsing, cleanup

def pckstat(args):
    """pckstat function for api calls."""
    print("Architecture: " + args.architecture)
    status_code = download_file(args.architecture)
    if status_code != 200:
        print("Error downloading file. Exiting...")
        return
    decompress_file(args.architecture)
    parsing(args.architecture)
    cleanup(args.architecture)

# Main function
def cli_main() -> None:
    """Main cli function."""
    # create the top-level parser
    parser = argparse.ArgumentParser(
      description="pckstat CLI tool for analyst."
    )

    parser.add_argument( # required positional argument
      "architecture", type=str,
        help="Architecture to download Contents file with."
    )

    parser.set_defaults(func=pckstat)

    # Parsing subcommands and arguments
    args = parser.parse_args()

    try:
        func = args.func # this would call the subfunctions based on what is passed into args
        func(args)
    except AttributeError as error:
        print(error, file=sys.stderr)
        parser.error("Give a subcommand")

if __name__ == "__main__":
    cli_main()
