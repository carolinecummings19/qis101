#!/usr/bin/env python3
"""ladder_problem.py"""

# Caroline Cummings - Task 10-01
# Calculate and display maximum ladder length

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from scipy.optimize import OptimizeResult  # type: ignore
    from numpy.typing import NDArray


def ladder_length(theta: NDArray[np.float_]) -> NDArray[np.float_]:
    """Function for finding ladder length given the angle"""
    return (2 / np.sin(theta)) + (1 / np.cos(theta)
)

def plot(ax: Axes) -> None:
    """Plots ladder length function and max point"""
    
    # Plot function - bounded from 0 to pi/2
    # Don't include start and end points to prevent dividing by 0 - from D. Biersach
    theta: NDArray[np.float_] = np.linspace(0, np.pi / 2, 100, dtype=np.float_)[1:-2]
    len: NDArray[np.float_] = ladder_length(theta)
    ax.plot(theta, len)

    # From SciPy.optimize module
    opt: OptimizeResult = scipy.optimize.minimize(ladder_length, np.pi / 4)  # type: ignore
    # Pull out x and y values
    x: float = opt.x  # type: ignore
    length: float = opt.fun  # type: ignore

    # Set plot title and labels
    ax.set_title(f"Ladder Length Function \n Max Length is {length:.4}")
    ax.set_xlabel("Angle (rad)")
    ax.set_ylabel("Length (m)")
    ax.set_ylim(0, 25)

    # Plot max point and label
    ax.plot(x, length, "bo")
    # Horizontal line - from D. Biersach
    ax.axhline(length, color="gray", linestyle="--")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()


#score 4
