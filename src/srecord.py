"""Main python starting script for Hex modification
"""
import os


class HexFile:
    """Class for funcionality of formatting srecord files, will be used also for another formats"""

    def __init__(self, file_path):
        print(rf"Hex file: {file_path}")
        self._file = file_path
        self._s19_records = self.analyse_s19(file_path)

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

    @property
    def s19_records(self):
        """Data from S19 file

        Returns:
            list: List of dictionaries of records
        """
        return self._s19_records

    def analyse_s19(self, file_path):
        """Analyser for s19 hex files and

        Args:
            file_path (str): Path to input file that will be analysed

        Returns:
            list: List that contains dictionary of hex data from s19 file
        """
        print("*** ANALYSING S19 FILE")
        file_data = []
        with open(file_path, "r", encoding="UTF-8") as file:
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
            print("*** DONE...")
            return file_data

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
        output = os.system(
            rf"{self.script_path}\src\MinGW\objcopy.exe -I {formats_dict[input_extension]}"
            + rf" -O {formats_dict[format_hex]} {file_path}"
            + rf" {os.path.dirname(file_path)}\{file_name}.{format_hex}"
        )
        if output == 0:
            return True
        else:
            return False

    def crc_check(self, data_hex):
        """Function to check crc checksum from data hex.

        Args:
            data_hex (str): Data from hex file

        Returns:
            str: CRC checksum
        """
        data_hex = data_hex.replace(":", "")
        sum_data = 0
        for i in range(0, int(len(data_hex) / 2)):
            byte = data_hex[i * 2 : (i * 2) + 2]
            sum_data += int("0x" + byte, 16)
        sum_data = hex(sum_data).replace("0x", "")
        sum_data = int("0x" + sum_data[-2:], 16)
        int_checksum = 0xFF - sum_data
        return "{0:0{1}x}".format(int_checksum, 2)

    def find_record_by_address(self, address):
        """Function to find record by address

        Args:
            address (str): address of record

        Returns:
            dict: Record of data
        """
        division_result = int(address, base=16) / 16 + 2
        print(self.s19_records[int(division_result) - 1])
        return self.s19_records[int(division_result) - 1]
