#!/usr/bin/env python3

import sys

for file in map( lambda arg: open(arg, 'r'), sys.argv[1:] ):
    print('\nReading file: {0}'.format(file.name))
    
    for line in file:
        print(line.rstrip())
