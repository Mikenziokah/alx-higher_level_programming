#!/usr/bin/python3
#!/usr/bin/python3
""" Create a new class Base """
from os import path
import json


class Base:
    """ New class base """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
