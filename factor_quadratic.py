#!/usr/bin/env python3
"""factor_quadratic.py"""

from math import gcd, sqrt

def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Jx^2 + Kx + L"""

    print(f"Given the quadratic: {h}x^2 + {i}x + {j}")

    """Keep track of whether polynomial is factorable with rationals"""
    is_factorable: bool = False

    for a in range(1, h + 1):
        if h % a == 0:
            c: int = h // a
            for b in range(1, j + 1):
                if j % b == 0:
                    d: int = j // b
                    if a * d + b * c == i:
                        print(f"The factors are: ({a}x + {b})({c}x + {d})")
                        is_factorable = True
                        """Stop displaying after first found factor"""
                        #return

    # Caroline Cummings - Task 04-03
    # Factoring GCD, processing negative coefficients, handle complex roots
    
    if not(is_factorable):
        print("Cannot be factored with rational numbers.")

        """Find GCD of h, i, j (factor out??)"""
        gcd_num: int = gcd(h, i, j)
        print(f"The GCD of {h}, {i}, and {j} is {gcd_num}")

        """Using quadratic formula: x = (-b +- sqrt(b^2 - 4ac)) / 2a"""
        if (i**2 - 4 * h * j) >= 0:
            x1: float = (-i + sqrt(i**2 - 4 * h * j)) / (2 * h)
            x2: float = (-i - sqrt(i**2 - 4 * h * j)) / (2 * h)
            print(f"The factors are: (x - ({x1: .4f})((x - ({x2: .4f}))")
        else:
            alpha: float = (-i) / (2 * h)
            beta: float = sqrt(abs(i**2 - 4 * h * j)) / (2 * h)
        
            print(f"The factors are: (x - ({alpha:.4f} + {beta:.4f}i)((x - ({alpha:.4f} - {beta:.4f}i))")
    print()

def main() -> None:
    factor_quadratic(115425, 3254121, 379020)

    """Task 04-03"""
    factor_quadratic(115425, 3254121, 379021)
    factor_quadratic(2, 6, 4)
    factor_quadratic(1, 0, 1)


if __name__ == "__main__":
    main()


#additional comments:

'''Really great job! Just a question, did you mean to comment out line 24?'''