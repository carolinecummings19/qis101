#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

# Caroline Cummings - Task 09-01
# Calculate and plot probability density function of 
# Maxwell-Boltzmann distribution

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.axes import Axes
from numpy.typing import NDArray
from math import sqrt, exp

# Found built-in maxwell distribution from: 
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.maxwell.html
from scipy.stats import maxwell # type: ignore

def maxwell_boltzmann_pdf(x: int, a: int) -> float:
    """PDF function - from Wiki page on MB Distribution"""
    return float((x**2 / a**3) * sqrt(2/np.pi) * exp(-x**2/(2*a**2)))

def plot(ax: Axes) -> None:
    """Plots PDF for 3 different parameters"""

    # Defines domain from 0 to 20
    x: NDArray[np.float_] = np.linspace(0, 20, 1000) 

    # Plot each graph using defined probability density function
    ax.plot(x, [maxwell_boltzmann_pdf(i, 1) for i in x], 'b-', label='a = 1')
    ax.plot(x, [maxwell_boltzmann_pdf(j, 2) for j in x], 'r-', label='a = 2')
    ax.plot(x, [maxwell_boltzmann_pdf(k, 5) for k in x], 'g-', label='a = 5')

    # Plot each graph - from scipy docs (creates same graph)
    """ax.plot(x, maxwell.pdf(x, scale=1), 'b-', label='a = 1')
    ax.plot(x, maxwell.pdf(x, scale=2), 'r-', label='a = 2')
    ax.plot(x, maxwell.pdf(x, scale=5), 'g-', label='a = 5')"""
    
    # Setting title, x- and y-axes, and legend
    ax.set_title("Maxwell-Boltzmann PDF Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.legend()
    ax.xaxis.set_major_locator(MultipleLocator(5))


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()



#additional comments

'''Suggest using a for loop to graph the 3 functions: 
# Parameters
a_values: list[int] = [1, 2,5]
# Plot the PDF for each value of "a"
for a in a_values:
    # Calculate the PDF
    pdf = maxwell.pdf(x, scale=a)
    # Plot the PDF
    plt.plot(x, pdf, label=f'a = {a}') '''


'''Score 4'''