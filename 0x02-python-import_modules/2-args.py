#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """prints command line arguments"""

    index = len(sys.argv) - 1
    if index == 0:
        print(index, "arguments.")
    elif index == 1:
        print("{} argument:". format(index))
    else:
        print("{} arguments:". format(index))

    if index >= 1:
        index = 0
        for arg in sys.argv:
            if index != 0:
                print("{}: {}". format(index, arg))
            index += 1
