#!/usr/bin/python3
""" function that reads a text file and prints it to sdout"""


def read_file(filename=""):
    """ reads UTF-8 file """
    with open(filename, encoding='utf-8') as my_file:
        my_file_read = my_file.read()
        print(my_file_read, end="")
