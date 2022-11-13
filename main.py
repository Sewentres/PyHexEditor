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

    else:
        Hex = HexFile(args.path)
        for data in Hex.s19_records:
            print(data)
