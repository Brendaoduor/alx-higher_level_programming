#!/usr/bin/python3
import hidden_4
import os
if __name__ == "__main__":
    
    folders = dir(hidden_4)
    for name in folders:
        if os.path.isfile(name) and name != '_':
            print(folders)
