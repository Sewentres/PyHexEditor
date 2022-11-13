"""Main python starting script for Hex modification
"""
import os
from unittest import TestLoader, TestResult
from pathlib import Path
from src import HexFile, ArgumentsInputs
from tests import TestRunner

if __name__ == "__main__":

    args = ArgumentsInputs()
    if args.unit_tests:
        unit_tests = TestRunner()

    Hex = HexFile(args.path)
    # for data in Hex.s19_records:
    #     print(data)
    Hex.find_record_by_address("0x045180")
    print(os.path.realpath(__file__))
