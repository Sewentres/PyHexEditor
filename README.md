# PyHexEditor

## PyHexEditor


## Convert bin to intel hex and motorola record:
We can convert binaries using prepared tool from MinGW32:
```bash
# For Intel Hex format
objcopy.exe -I binary -O ihex "PyHexEditor\example\Example.bin" "PyHexEditor\example\test.hex"
# For Motorola Hex format
objcopy.exe -I binary -O srec "PyHexEditor\example\Example.bin" "PyHexEditor\example\test.s19"
```