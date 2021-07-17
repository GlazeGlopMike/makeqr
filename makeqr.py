import getopt
import pyqrcode
import os.path
import re
import sys

def main(argv):
    # options
    forceoverwrite = False
    fromfile = False
    ofile = ""
    txtin = ""

    # get arguments
    try:
        opts, args = getopt.gnu_getopt(argv, "fho:x")
    except getopt.GetoptError:
        print("Usage: makeqr.py [-f] input [-o outputfile] [-h] [-x]")
        sys.exit(2)

    # process arguments
    for opt, arg in opts:
        if opt == "-f":
            fromfile = True
        elif opt == "-o":
            ofile = arg
        elif opt == "-h":
            print("Generates QR codes in SVG format.")
            print("Usage: qrgen.py [-f] input [-o outputfile] [-h] [-x]")
            print()
            print("-f    Treat input as a file path")
            print("-h    Display the usage syntax")
            print("-o    Specify the destination")
            print("-x    Overwrite without prompt")
        elif opt == "-x":
            forceoverwrite = True

    # get text source
    try:
        if fromfile:
            with open(args[0], 'r') as file:
                txtin = file.read()
        else:
            txtin = args[0]
    except FileNotFoundError:
        print("ERROR: Input file not found.")
        sys.exit(2)
    except IndexError:
        if fromfile:
            print("ERROR: No text source provided.")
            sys.exit(2)
        else:
            txtin = input("Text to encode: ")

    # generate filepath
    if ofile == "" and fromfile:
        ofile = os.path.splitext(args[0])[0] + ".svg"
    else:
        ofile = re.sub('[^0-9a-zA-Z]+', '-', txtin[:20]).rstrip("-") + ".svg"
    
    if not forceoverwrite and os.path.isfile(ofile):
        conf = input(f"Overwrite existing file '{ofile}'? (Y/N) ")
        if conf.upper() != 'Y':
            print("ERROR: Overwrite permission not granted, process aborted.")
            sys.exit(3)

    # save QR code
    try:
        code = pyqrcode.create(txtin) 
        code.svg(ofile, scale = 8)
        print("Generated QR code image " + ofile)
    except OSError:
        print("ERROR: Illegal destination provided, process failed.")
    except UnicodeEncodeError:
        print("ERROR: Illegal character in source, process failed.")

if __name__ == "__main__":
    main(sys.argv[1:])
