#!/usr/bin/env python3

import fileinput

for line in fileinput.input(): 
    if fileinput.isfirstline():
        print("\nReading File: {0}".format(fileinput.filename()))
    print(line, end="")
