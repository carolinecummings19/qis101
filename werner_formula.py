#!/usr/bin/env python3
"""nyquist_unknown.ipynb"""

# Task 12-02
# Caroline Cummings 

from __future__ import annotations

import typing
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def plot(ax: Axes) -> None:
    """Graph 4 functions over [-3pi, 3pi]"""
    x: NDArray[np.float_] = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
    
    # Plot f1 = sin(0.8x)
    f1: NDArray[np.float_] = np.sin(0.8 * x)
    ax.plot(x, f1, label="$f_1(x) = sin(0.8x)$")

    # Plot f2 = sin(0.5x)
    f2: NDArray[np.float_] = np.sin(0.5 * x)
    ax.plot(x, f2, label="$f_2(x) = sin(0.5x)$")

    # Plot f3 = f1 * f2
    ax.plot(x, f1 * f2, label="$f_3(x) = f_1(x) * f_2(x)$")

    # Plot f4 = Werner's formula for f1 * f2 - from Wolfram MathWorld
    x4: NDArray[np.float_] = np.linspace(-3 * np.pi, 3 * np.pi, 50)
    f4: NDArray[np.float_] = 1 / 2 * (np.cos(0.3 * x4) - np.cos(1.3 * x4))
    ax.plot(x4, f4, label=r"$f_4(x) = \frac{1}{2} (cos(0.3x) - cos(1.3x))$", ls="--", \
            color="lightgray", marker=MarkerStyle('o'), markersize=4) 

    # Label graph
    ax.set_title(r"Werner Formula")
    ax.set_ylabel('$y$')
    ax.set_xlabel('$x$')
    ax.legend(loc="upper right")
    ax.set_ylim(top=1.75)
    ax.grid(True)

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()

if __name__ == "__main__":
    main()


#score 4