# makeqr
A quick-and-dirty QR code generator using the [pyqrcode](https://pypi.org/project/PyQRCode/) module. QR codes are saved as Scalable Vector Graphics (SVG) files.

## Installation
Using pip:
```pip3 install pyqrcode```

## Usage
Generating from a string:
- ```python3 makeqr.py "sample text"```

Generating from an input file:
- ```python3 makeqr.py -f source.txt```

Specifying an output location:
- ```python3 makeqr.py -f source.txt -o dest.svg```
- Force overwrite: ```python3 makeqr.py -f source.txt -x -o dest.svg```
