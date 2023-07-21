#!/usr/bin/env python3
"""plot_ellipse.py"""

# Caroline Cummings - Task 06-01
# Display 2D graph of ellipse

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot_ellipse(ax: Axes) -> None:
    """Plot a ellipse: major axis of a=100, minor axis of b=50"""
    a: float = 100.0
    b: float = 50.0
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)

    # Polar to Cartesian coordinate conversion using vectorized operations
    x: NDArray[np.float_] = a * np.cos(theta)
    y: NDArray[np.float_] = b * np.sin(theta)

    ax.plot(x, y)

    # Had a hard time figuring out the LaTex - from D. Biersach
    ax.set_title(rf"$ \frac{{x^2}}{{{int(a)}^2}} + \frac{{y^2}}{{{int(b)}^2}} = 1$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    # Setting locators - from D. Biersach
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(10))

    ax.set_aspect("equal")



def main() -> None:
    plt.figure(__file__)
    plot_ellipse(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()



#Additional comments
'''Score 4'''