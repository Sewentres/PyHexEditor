"""Unit test module for testing purposes
"""

import unittest
import sys
import os

sys.path.append("../")
from src.srecord import HexFile

FILE_DIR = os.path.dirname(os.path.realpath(__file__))


class TestStringMethods(unittest.TestCase):
    def test_crc_check(self):
        Hex = HexFile(FILE_DIR + "\\..\\example\\test.s19")
        self.assertEqual(
            Hex.crc_check("140451704060522040A45E2040C089FE3F28F0FE"), "d6"
        )
        self.assertEqual(
            Hex.crc_check("140451803F0000000000000000000000000000BB"), "1c"
        )
        self.assertEqual(
            Hex.crc_check("1404516040985E204018112040FC2F2040AC4E20"), "72"
        )
        self.assertEqual(
            Hex.crc_check("1404514040501F2040982B2040F02F20402C3720"), "22"
        )
        self.assertEqual(
            Hex.crc_check("14045060001C002E6C6F63616C00000000E00000"), "02"
        )

    def test_find_record(self):
        Hex = HexFile(FILE_DIR + "\\..\\example\\test.s19")
        self.assertEqual(Hex.find_record_by_address("045180")["crc"], "1C")
        self.assertEqual(
            Hex.find_record_by_address("0x045120")["data"],
            "6300232D302B2000686C4C0065666745",
        )
        self.assertEqual(
            Hex.find_record_by_address("0x0000045120")["address"],
            "045120",
        )
        self.assertEqual(
            Hex.find_record_by_address("44FD0")["crc"],
            "7E",
        )
        self.assertEqual(
            Hex.find_record_by_address("044F60")["crc"],
            Hex.crc_check(
                Hex.find_record_by_address("044F60")["count"]
                + Hex.find_record_by_address("044F60")["address"]
                + Hex.find_record_by_address("044F60")["data"]
            ),
        )


if __name__ == "__main__":
    unittest.main()
