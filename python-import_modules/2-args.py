#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    NoA = len(argv)
    if NoA == 1:
        print("0 arguments.")
    elif NoA == 2:
        print("1 argument:")
        for i in range(1, len(argv)):
            print("{}: {}". format(i, argv[i]))
    else:
        print("{} arguments:".format (NoA -1))
        for i in range(1, len(argv)):
            print("{}: {}". format(i, argv[i]))
 