#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=" ")
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
