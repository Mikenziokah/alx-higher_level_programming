#!/usr/bin/python3
""" savin to json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes an Object to
    a text file, using a JSON representation:"""
    with open(filename, 'w',) as my_file:
        json.dump(my_obj, my_file)
