#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_a = []
    for i in range(list_length):
        try:
            list_b = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            list_b = 0
        except (ZeroDivisionError):
            print("division by 0")
            list_b = 0
        except (IndexError):
            print("out of range")
            list_b = 0
        finally:
            list_a.append(list_b)
    return (list_a)
