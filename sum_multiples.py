#!/usr/bin/env python3
"""sum_multiples.py"""

# Caroline Cummings - Task 03-03

# Sums all natural numbers less than 1900 divisible by both 7 and 11

def is_divisible(n: int, d1: int, d2: int) -> bool:
    """Determines if n is divisible by two divisors"""
    return n % d1 == 0 and n % d2 == 0


def main() -> None:
    sum: int = 0
    for num in range(0, 1_900):
        if is_divisible(num, 7, 11):
            sum += num
    print(f"{sum:>7,}")        


if __name__ == "__main__":
    main()



#additional comments:

'''Avoid performing longer calculations in the Main function. ''' 

 