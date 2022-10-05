"""Main python starting script for Hex modification
"""


class HexFile:
    """Class for funcionality of formatting srecord files, will be used also for another formats"""

    def __init__(self, File_Path):
        print(rf"Hex file: {File_Path}")
        self.File = File_Path

    def format_file(self):
        print("test")
