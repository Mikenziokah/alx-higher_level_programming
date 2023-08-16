#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        high_value = max(a_dictionary, key=a_dictionary.get)
        return (high_value)
