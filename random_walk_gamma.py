#!/usr/bin/env python3
"""random_walk_gamma.py"""

# Caroline Cummings - Task 06-02
# Plots expected final distance of uniform random walk N on unit 
# lattice of dim d

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma #type: ignore
from math import sqrt

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def expected_distance(d: float, num_steps: int) -> float:
    """Returns the expected distance for dimension d and steps num_steps"""
    # Split up formula into two terms 
    term1: float = sqrt(2 * num_steps / d)
    term2: float = float((gamma((d + 1) / 2) / gamma(d / 2)) ** 2) #type: ignore
    
    return term1 * term2

def main() -> None:
    # Number of steps
    n: int = 20000  

    # Dimensions from 1 to 25
    dims: NDArray[np.float_] = np.arange(1, 26, dtype=np.float_)  

    # Calculate expected distances with dimensions in range
    expected_distances: list[float] = [expected_distance(d, n) for d in dims]

    # Create and label plot
    ax: Axes = plt.subplot()
    ax.plot(dims, expected_distances)
    ax.set_title("Expected Final Distance of Uniform Random Walk")
    ax.set_xlabel("Dimension (d)")
    ax.set_ylabel("Expected Distance")
    ax.plot()

    plt.show()

if __name__ == "__main__":
    main()



#Additionl comments
'''Score 4'''