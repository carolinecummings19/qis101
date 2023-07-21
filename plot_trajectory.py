#!/usr/bin/env python3
"""plot_trajectory.py"""

# Task 16-02
# Caroline Cummings
# Plot particle data from ray.csv and best fit line

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot(ts: NDArray[np.float_], hs: NDArray[np.float_], ax: Axes) -> None:
    ax.set_title("Particle's Path")

    ax.set_xlabel("Time")
    ax.set_ylabel("Height")

    ax.scatter(ts, hs, s=10)

    # Find line of best fit - https://www.statology.org/line-of-best-fit-python/
    a, b = np.polyfit(ts, hs, 1)

    # Add line of best fit to plot
    ax.plot(ts, a*ts + b, color="red") 

def main() -> None:
    data: NDArray[np.float_] = np.genfromtxt("Session 16 - Scientific Computing/ray.csv", comments='#', delimiter=",")
    # Time samples (first column in file)
    time: NDArray[np.float_] = data[:, 0]
    # Height samples (second column in file)
    height: NDArray[np.float_] = data[:, 1]

    plt.close("all")

    # Plot data 
    plt.figure("ray.csv")
    plot(time, height, plt.axes())
    plt.show()

if __name__ == "__main__":
    main()