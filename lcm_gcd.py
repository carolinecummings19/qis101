#!/usr/bin/env python3
"""lcm_gcd.py"""

# Caroline Cummings - Task 04-01

# Calculate lowest common multiple of two integers
# no loops, use gcd
# Display LCM of 447618, 2011835

from math import gcd

def main() -> None: 
    """Declare variables for two integers and gcd"""
    num1: int = 447618
    num2: int = 2011835
    gcd_num: int = gcd(num1, num2)

    """Find lcm by multiplying nums and dividing out gcd"""
    lcm_num: int = int((num1 * num2) / gcd_num)
    
    print(f"The least common multiple of {num1} and {num2} is {lcm_num}")

if __name__ == "__main__":
    main()