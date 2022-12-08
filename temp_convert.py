#!/usr/bin/env python3

# Created By: Jessah
# Date: December 07, 2022
# This program ask the user for a temperature in celsius
# and it will convert to a fahrenheit using functions


def fahrenheit():
    # get input from user
    celsius_str = input("Enter a temperature in celsius: ")
    # try catch for strings
    try:
        celsius = float(celsius_str)
    except Exception:
        print("{} is invalid".format(celsius_str))
    else:
        # formula for celsius to fahrenheit
        multiply = celsius * 1.8
        to_fahrenheit = multiply + 32
        # display to user
        print("{} in fahrenheit is {:.2f}".format(celsius, to_fahrenheit))


def main():
    # call fahrenheit function
    fahrenheit()


if __name__ == "__main__":
    main()
