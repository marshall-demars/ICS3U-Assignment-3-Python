#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program calculates the average of 3 numbers
#    with user input


def main():
    # this calculates the average of 3 numbers

    # input
    number_one = float(input("Enter a number between 1 and 100: "))
    number_two = float(input("Enter a number between 1 and 100: "))
    number_three = float(input("Enter a number between 1 and 100: "))

    # process and output
    if number_one > 100:
        print("\nPlease input a number between 1 and 100.")
    elif number_two > 100:
        print("\nPlease input a number between 1 and 100.")
    elif number_three > 100:
        print("\nPlease input a number between 1 and 100.")
    elif number_one < 0:
        print("\nPlease input a number between 1 and 100.")
    elif number_two < 0:
        print("\nPlease input a number between 1 and 100.")
    elif number_three < 0:
        print("\nPlease input a number between 1 and 100.")
    else:
        average = (number_one + number_two + number_three) / 3
        print("\nThe average is {0}!".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
