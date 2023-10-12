#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = []
    values = []
    for x, y in a_dictionary.items():
        keys.append(x)
        values.append(y)
    keys.sort()
    for i in keys:
        print("{}: {}".format(i, a_dictionary[i]))
