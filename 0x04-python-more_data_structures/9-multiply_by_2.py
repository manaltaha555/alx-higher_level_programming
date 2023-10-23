#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    keys = a_dictionary
    values = a_dictionary.values()
    new = dict(zip(keys, map(lambda x: x * 2, values)))
    return new
