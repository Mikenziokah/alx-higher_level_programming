#!/usr/bin/python3
""" function that reads a text file and prints it to sdou"""
def read_file(filename=""):
    """ reads UTF8 file """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
