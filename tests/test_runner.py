from unittest import TestLoader, TestResult
from pathlib import Path
import os


class TestRunner:
    def __init__(self):
        self.test_run()

    def test_run(self):
        test_loader = TestLoader()
        test_result = TestResult()

        test_directory = str(os.path.dirname(Path(__file__).resolve()))
        print(test_directory)
        test_suite = test_loader.discover(test_directory, pattern="test_*.py")
        test_suite.run(result=test_result)
        final_output = "Tests run: {}.  ".format(
            test_result.testsRun
        ) + "Errors: {}  Failures: {}.".format(
            len(test_result.errors), len(test_result.failures)
        )
        print("************************************************")
        print("***")
        print("*** " + final_output)
        print("***")
        print("************************************************")

        if test_result.wasSuccessful():
            exit(0)
        else:
            exit(-1)
