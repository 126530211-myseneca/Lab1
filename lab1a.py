#!/usr/bin/env python3

from datetime import datetime

def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        present_year = datetime.now().year
        age = present_year - birth_year
        return age
    except ValueError:
        print("Please enter an int")

def helloWorld():
    print("Hello World")

age = calculate_age()
print("Your age is:", age)
helloWorld()
