"""Main python starting script for Hex modification
"""
import argparse
from src.srecord import HexFile


def cmdline_args():
    """Parser for input arguments.

    Returns:
        object: all parsered arguments.
    """
    # Make parser object
    parser = argparse.ArgumentParser(
        description="", formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--PATH", help="Path to hex file")

    return parser.parse_args()


if __name__ == "__main__":

    args = cmdline_args()
    Hex = HexFile(args.PATH)
    Hex.format_file(Hex.file_name, "INTEL")
