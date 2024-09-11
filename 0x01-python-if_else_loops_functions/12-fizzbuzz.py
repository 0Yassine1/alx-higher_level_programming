#!/usr/bin/python3
# Function to print numbers from 1 to 100 with Fizz, Buzz, and FizzBuzz substitutions

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
