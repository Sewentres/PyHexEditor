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
            rf"{self.script_path}\src\MinGW\objcopy.exe -I {formats_dict[input_extension]}"
            + rf" -O {formats_dict[format_hex]} {file_path}"
            + rf" {os.path.dirname(file_path)}\{file_name}.{format_hex}"
        )

    def analyse_s19(self, file_path):
        """Analyser for s19 hex files and

        Args:
            file_path (str): Path to input file that will be analysed

        Returns:
            list: List that contains dictionary of hex data from s19 file
        """
        print("TESTING ANALYSING S19 FILES")
        file_data = []
        file = open(file_path, "r", encoding="UTF-8")
        lines = file.readlines()
        for line in lines:
            data = line[:-1]
            if data[1:2] == "0":
                address = "0000"
                address_length = 8
                data_hex = data[address_length:-2]
            if data[1:2] == "1" or data[1:2] == "9":
                address_length = 8
                address = data[4:address_length]
                data_hex = data[address_length:-2]
                if data[1:2] == "9":
                    data_hex = ""
            if data[1:2] == "2" or data[1:2] == "8":
                address_length = 10
                address = data[4:address_length]
                data_hex = data[address_length:-2]
                if data[1:2] == "8":
                    data_hex = ""
            if data[1:2] == "3" or data[1:2] == "7":
                address_length = 12
                address = data[4:address_length]
                data_hex = data[address_length:-2]
                if data[1:2] == "7":
                    data_hex = ""
            data = {
                "type": data[0:2],
                "count": data[2:4],
                "address": address,
                "data": data_hex,
                "crc": data[-2:],
            }
            file_data.append(data)
        return file_data
