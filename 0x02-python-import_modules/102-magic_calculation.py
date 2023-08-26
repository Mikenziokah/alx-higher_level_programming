#!/usr/bin/python3
from magic_caculation_102 import add, sub
def magic_caculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return (c)
        else:
            return sub(a, b)
