#!/usr/bin/env python3
"""benfords_law.py"""

# Caroline Cummings - Task 09-01
# Law of Anomalous Numbers 
# Calculate probability of each digit (1-9) for 100,000 random numbers

from __future__ import annotations

import typing
import random

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

# Used chatGPT for initializing frequencies for matplotlib
def plot_benfords(ax: Axes, data: list[int]) -> None:
    """Plots frequency of each digit as most significant digit"""
    digits = range(1, 10)
    frequencies: list[float] = [data.count(digit) / len(data) for digit in digits]
    
    # Use matplotlib bar plot to plot bars 
    ax.bar(digits, frequencies)
    ax.set_title("Benford's Law of Anomalous Numbers")
    ax.set_xlabel("Digit")
    ax.set_ylabel("Probability")

    ax.xaxis.set_major_locator(MultipleLocator(1))

def main() -> None: 
    random.seed(2022)

    # Get most significant digit
    sig_digs: list[int] = []
    for _ in range(100000):
        number: int = random.randint(1, 1000000)
        first: str = str(number**100)[0]
        result = int(first)
        sig_digs.append(result)


    plt.figure(__file__)
    plot_benfords(plt.axes(), sig_digs)
    plt.show()

if __name__ == "__main__":
    main()




#additional comments
'''Score 4'''