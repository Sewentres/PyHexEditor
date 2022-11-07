"""Main python starting script for Hex modification
"""
import argparse
from src import HexFile
import os


def cmdline_args():
    """Parser for input arguments.

    Returns:
        object: all parsered arguments.
    """
    # Make parser object
    parser = argparse.ArgumentParser(
        description="", formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--PATH", help="Path to hex file", required=True)

    return parser.parse_args()


if __name__ == "__main__":

    args = cmdline_args()
    Hex = HexFile(args.PATH)
    # for data in Hex.s19_records:
    #     print(data)
    Hex.find_record_by_address("0x045180")
    print(os.path.realpath(__file__))
