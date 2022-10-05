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
        return os.path.splitext(os.path.basename(self._file))[0]

    @property
    def file_extension(self):
        """Extension of hex file

        Returns:
            string: Striped extension of file
        """
        return os.path.splitext(os.path.basename(self._file))[1]

    @property
    def script_path(self):
        """Path to script

        Returns:
            string: Path to script
        """
        return os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    def format_file(self, file_path, format_hex):
        """Function to convert a hex file to different format like Intel Hex,
        Motorola Srecord or Binary.

        Args:
            file_path (str): Path to input file
            format_hex (str): Format of output file
        """
        formats_dict = {"hex": "ihex", "s19": "srec", "bin": "binary"}
        input_extension = os.path.splitext(os.path.basename(file_path))[1][1:]
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        os.system(
            rf"{self.script_path}\src\MinGW\objcopy.exe -I {formats_dict[input_extension]} -O {formats_dict[format_hex]} {file_path} {os.path.dirname(file_path)}\{file_name}.{format_hex}"
        )
