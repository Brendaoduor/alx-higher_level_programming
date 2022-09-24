#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """prints command line arguments"""

    index = len(sys.argv)
    if sys.argv[0]:
        print(index, "arguments.")
    elif index == 1:
        print("{} arguments:".format(index))
