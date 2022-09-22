#!/usr/bin/python3
import hidden_4
folders = dir(hidden_4)
for name in folders:
    if name[:2] != '__':
        print(name)
