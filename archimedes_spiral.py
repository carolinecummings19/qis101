#!/usr/bin/env python3
"""archimedes_spiral.py"""

# Caroline Cummings - Task 10-02
# Calculate and display arc length of archimedes spiral

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
# Found from SciPy docs on scipy.integrate
from scipy.integrate import quad # type: ignore
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from numpy.typing import NDArray

def spiral_arc_length (r: float) -> float:
    """Arc length formula to integrate"""
    return sqrt(r**2 + 1)

def main() -> None:
    start = 0
    end = 8*np.pi

    # Calculate arc length using formula and built-in integration 
    length, err = quad(spiral_arc_length, start, end)
    print(f"Length of Archimedes Spiral r = θ from 0 to 8π is {length}")

    # Graphing spiral 
    theta: NDArray[np.float_] = np.linspace(start, end, 1000)
    
    # From matplotlib.org on graphing with plt.polar 
    # Takes input of theta and r (r = theta)
    plt.polar(theta, theta)
    plt.show()


if __name__ == "__main__":
    main()



#Additional comments
'''Awesome job and well labeled graph'''
'''Score 5'''