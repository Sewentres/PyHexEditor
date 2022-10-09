import unittest
import sys

sys.path.append("../")
from src.srecord import HexFile


class TestStringMethods(unittest.TestCase):
    # def test_upper(self):
    #     self.assertEqual("foo".upper(), "FOO")

    # def test_isupper(self):
    #     self.assertTrue("FOO".isupper())
    #     self.assertFalse("Foo".isupper())

    # def test_split(self):
    #     s = "hello world"
    #     self.assertEqual(s.split(), ["hello", "world"])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    def test_crc_check(self):
        Hex = HexFile("Test/path")
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


if __name__ == "__main__":
    unittest.main()
