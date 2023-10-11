#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list == []:
        return 0
    my_set = set(my_list)
    sum = 0
    for i in my_set:
        sum += i
    return sum
