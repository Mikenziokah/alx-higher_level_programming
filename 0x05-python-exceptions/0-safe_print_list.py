#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
        number = 0
        for i in range(x):
                try:
                        print("{}".format(my_list[i]), end="")
                except IndexError:
                        break
                else:
                        number += 1

        print()
        return (number)
