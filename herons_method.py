#!/usr/bin/env python3
"""herons_method.py"""

# Caroline Cummings - Task 04-02

# Using Heron's Method to estimate square roots
# use random, find r s.t. r = sqrt(s) + e for e<10^-8

from random import randint

def main() -> None: 
    """Generate random num s using randint"""
    s: int = randint(10**6, 2*(10**6))

    """Find r using initial guess x0 and revised guess x"""
    x0: float = s / 2
    x: float = x0 + (s - x0**2) / (2 * x0)
    r: float = x

    epsilon: float = 1e-8

    while abs(s-r**2) > epsilon:
        r = x + (s - x**2) / (2 * x)
        x = r

    print(f"The estimated square root of s = {s} using Heron's method is r = {r:.8f}")

if __name__ == "__main__":
    main()