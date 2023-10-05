#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for folders in dir(hidden_4):
        if folders[0] != '_' and folders[1] != '_':
            print(folders)
