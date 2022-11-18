import argparse


class ArgumentsInputs:
    """Class for arguments from user"""

    def __init__(self):
        self.cmdline_args()

    def cmdline_args(self):
        """Parser for input arguments.

        Returns:
            object: all parsered arguments.
        """
        # Make parser object
        parser = argparse.ArgumentParser(
            description="", formatter_class=argparse.RawDescriptionHelpFormatter
        )

        parser.add_argument("--PATH", help="Path to hex file", required=False)
        parser.add_argument(
            "--DEBUG",
            help="Debug mode for testin purposes",
            required=False,
            action=argparse.BooleanOptionalAction,
        )
        parser.add_argument(
            "--UNITTESTS",
            help="Flag to perform unit tests",
            required=False,
            action=argparse.BooleanOptionalAction,
        )
        arg = parser.parse_args()
        self.path = arg.PATH
        self.unit_tests = arg.UNITTESTS
        self.debug = arg.DEBUG
        if not self.unit_tests and not self.path and not self.debug:
            print("************************************************")
            print("*** Path to binary file was not given")
            print(
                "*** Provide path to binary file using parameter --PATH <path_to_file>"
            )
            print("*** Use --UNITTESTS parameter to run available unit tests")
            print("*** Or use --DEBUG parameter to run DEBUG mode")
            print("************************************************")
            exit(1)
        return True
