#!/usr/bin/python3
""" inherits from a list """


class MyList(list):
    """ Mylist class that inherist from list """

    def print_sorted(self):
        """ Fucntion that prints a sorted list """
        print(sorted(self))
