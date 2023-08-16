#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        new = a_dictionary.copy()
        new[i] = a_dictionary[i] * 2
        return (new)
