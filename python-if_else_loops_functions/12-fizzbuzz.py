#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 100):
        print(i, end=" ")

        if i % 3:
            print("Fizz")
        elif i % 5:
            print("Buzz")
        elif i % 10:
            print("Fizz Buzz")
