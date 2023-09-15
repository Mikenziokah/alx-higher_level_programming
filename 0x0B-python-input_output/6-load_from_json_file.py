#!/usr/bin/python3
""" load from json """
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”:"""
    with open(filename, 'r') as my_file:
        return (json.load(my_file))
