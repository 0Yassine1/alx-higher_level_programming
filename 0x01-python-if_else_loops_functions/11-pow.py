#!/usr/bin/python3
# Function to compute a to the power of b

def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    else:  # b < 0
        result = 1
        for _ in range(-b):
            result *= a
        return 1 / result
