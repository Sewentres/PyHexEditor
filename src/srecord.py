"""Main python starting script for Hex modification
"""
import os


class HexFile:
    """Class for funcionality of formatting srecord files, will be used also for another formats"""

    def __init__(self, file_path):
        print(rf"Hex file: {file_path}")
        self._file = file_path

    @property
    def file(self):
        """Path to hex file

        Returns:
            string: Path to file
        """
        return self._file

    @property
    def file_name(self):
        """Name of hex file

        Returns:
            string: Striped name of file
        """
        return os.path.basename(self._file)

    def format_file(self, file_path, format_hex):
        """Function to convert a hex file to different format like Intel Hex,
        Motorola Srecord or Binary.

        Args:
            file_path (str): Path to input file
            format_hex (str): Format of output file
        """
        print(rf"Input file = [{file_path}]")
        print(rf"Format_hex = [{format_hex}]")
