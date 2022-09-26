import sys
import argparse


def cmdline_args():
    # Make parser object
    p = argparse.ArgumentParser(
        description="", formatter_class=argparse.RawDescriptionHelpFormatter
    )

    p.add_argument("--PATH", help="Path to hex file")

    return p.parse_args()


if __name__ == "__main__":

    args = cmdline_args()
    print(args.PATH)
