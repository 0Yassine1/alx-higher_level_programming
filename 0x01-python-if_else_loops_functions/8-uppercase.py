#!/usr/bin/python3
# Function to print a string in uppercase

def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
