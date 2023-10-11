#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list == [] or search == None:
         return None
    count = my_list.count(search)
    if count == 0:
         return my_list
    new = my_list.copy()
    for i in range(len(new)):
         if new[i] == search:
            new[i] = replace
    return new            
