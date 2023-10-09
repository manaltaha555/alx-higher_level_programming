#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    for i in range(2):
        new_tuple.append(tuple_a[i] + tuple_b[i])
    new_tuple = tuple(new_tuple)
    return new_tuple
