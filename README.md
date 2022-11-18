# PyHexEditor

## PyHexEditor is just a module for handling binary files in SRecord and Intel Format

This module is written only for training purpose to develop skills in Python Programing Language.\
As funcionallity using this module we will able to modify binary files like:
* Adding new data in specific address location
* Moving data to other address location
* Filling gaps between blocks of data
* Saving modificated binary file to specific format

## Current funcionallity:
* Display loaded S19 file
* Calculate Checksum of all records
* Finding data by address location

## Convert bin to intel hex and motorola record:
We can convert binaries using prepared tool from MinGW32\
This is just information for testing purposes.
```bash
# For Intel Hex format
objcopy.exe -I binary -O ihex "PyHexEditor\example\Example.bin" "PyHexEditor\example\test.hex"
# For Motorola Hex format
objcopy.exe -I binary -O srec "PyHexEditor\example\Example.bin" "PyHexEditor\example\test.s19"
```