#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """prints command line arguments"""

    index = len(sys.argv) - 1
    if index == 0:
        print(index, "arguments.")
    elif index == 1:
        print(index, "arguments:")
    else:
        print("{} arguments:".format(index))
    for indx in range(index):
        print("{} : {}".format(indx + 1, sys.argv[indx + 1]))
