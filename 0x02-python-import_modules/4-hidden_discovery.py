#!/usr/bin/python3
import hidden_4.phc
if __name__ == "__main__":
    folders = [name for name in os.listdir(".")
               if os.path.isdir(name) and name != '_']
    print(dir(hidden_4.phc))
