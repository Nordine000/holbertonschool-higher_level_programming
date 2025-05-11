#!/usr/bin/python3
def print_last_digit(number):
    last_number = abs(number) % 10 if number >= 0 else -(abs(number) % 10)
    print(f"Last digit of {number} is {last_number}", end=" ")
