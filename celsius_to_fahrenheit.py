#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""

# Caroline Cummings - Task 03-01

# Converts range of temperatures from Celsius to Fahrenheit 
# Temperatures from -44 - 106 degrees Celsius in steps of 4 (use range)

def main() -> None:
    for celsius in range(-44, 107, 4):
        fahrenheit: float =  (celsius * 9 / 5) + 32
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")
    

if __name__ == "__main__":
    main()


#Additional Comments:
'''Well documented, nice job!'''