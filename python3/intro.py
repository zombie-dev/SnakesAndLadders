#!/usr/bin/env python3

# Python required that functions be defined before being called

def greet(name):
    print('Hey there: {0}'.format(name))

name = input("Who's there? ")

greet(name)
