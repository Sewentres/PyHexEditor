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
    print("TESTING FILE FORMATING")
    Hex.format_file(Hex.file, "hex")
    print("TESTING FILE ANALYSING")
    print(Hex.analyse_s19(Hex.file))
    print(Hex.crc_check("140451704060522040A45E2040C089FE3F28F0FE"))
