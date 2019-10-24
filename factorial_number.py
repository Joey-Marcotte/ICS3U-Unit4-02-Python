#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows the factorial of a number


def main():
    # input
    multiplied_number = 1
    total_number = 1
    number = input("Input the number: ")

    try:
        number_as_number = int(number)
        while number_as_number > multiplied_number:
            # process
            print("x{0}".format(multiplied_number))
            multiplied_number = multiplied_number + 1
            total_number = multiplied_number * total_number

        print("x{0}".format(number_as_number))
        print("The answer is {0}".format(total_number))

    except(ValueError):
        print("That is not a valid number")


if __name__ == "__main__":
    main()
