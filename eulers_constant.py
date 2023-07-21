#!/usr/bin/env python3
"""eulers_constant.py"""

# Caroline Cummings - Task 10-03
# Numerically estimates Euler's constant (0.5772156649)
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad # type: ignore
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def gamma_function(x: float) -> float: 
    """Function to integrate over"""
    return -float(np.log(np.log(1 / x)))

def harmonic_number(n: int) -> float:
    """Calculates the n-th harmonic number - from chatGPT"""
    return sum(1 / i for i in range(1, n+1))

def plot(ax: Axes, constant: float) -> None: 
    # Generate the first 50 harmonic numbers - from chatGPT
    n_values = range(0, 51)
    harmonic_values: list[float] = [harmonic_number(n) for n in n_values]

    # Create the step plot - from plt.step docs
    ax.step(n_values, harmonic_values, where='mid')

    # Calculate and create the natural log graph
    x: NDArray[np.float_] = np.linspace(0, 50, 100)
    np.seterr(divide="ignore") # Deal with divide by zero runtime error
    log_x: NDArray[np.float_] = np.log(x)
    np.seterr(divide="warn")
    y = [constant + n for n in log_x]
    ax.plot(x, y)

    # Set plot title and labels
    ax.set_title(r"Graph of $\gamma + lnx$ and Step Plot of Harmonic Numbers")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    

def main() -> None:
    #From SciPy.integrate module
    constant, err = quad(gamma_function, 0, 1)
    print(f"My numerical estimate of Euler's constant is {constant}")

    plt.figure(__file__)
    plot(plt.axes(), float(constant))
    plt.show()


if __name__ == "__main__":
    main()


#score 4