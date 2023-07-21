#!/usr/bin/env python3
"""hamming_weight.py"""

# Caroline Cummings - Task 05-01

"""Implements a function to calculate population count of a given int"""
"""Calculate hamming weight of 95,601 & compare with python"""

def hamming_weight(num: int) -> int:
    """Returns the number of 1's (h_count) in the binary of a decimal number"""
    h_count: int = 0

    while num >= 1:
        if (num % 2 ==0):
            num = int(num / 2)
        else: 
            num = int(num / 2)
            h_count += 1
    return h_count


def main() -> None:
    x: int = 95601

    print(f"The population count of {x:,} is {hamming_weight(x)}")

    """Python's built in pop count (found on stack overflow)"""
    p_count: int = bin(x).count("1")
    print(f"Python says population count of {x:,} is {p_count}")

if __name__ == "__main__":
    main()