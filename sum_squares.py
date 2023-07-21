#!/usr/bin/env python3
"""sum_squares.py"""

# Caroline Cummings - Task 03-02

# Sums first 1000 natural numbers squared
# Also displays value using functional equation for Gaussian elimination

def square_summation(n: int) -> float:
    """Sums each integer squared from 1 to n inclusive"""
    sum: float = 0.0
    for k in range(1, n + 1):
        sum += k**2
    return sum


def main() -> None:
    nums: int = 1_000

    """Loop Sum"""
    sum: float = square_summation(nums)
    print(f"{sum:>7,}")

    """Functional equation"""
    fun_eq: float = 1/6 * nums * (nums + 1) * ((2 * nums) + 1)
    print(f"{fun_eq:>7,}")


if __name__ == "__main__":
    main()