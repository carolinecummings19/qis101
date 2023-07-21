#!/usr/bin/env python3
"""euler_curve.py"""

# Task 17-02
# Caroline Cummings
# Plots 2D parametric curve from [0, 12.34] and displays arc length

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def x_t (u: float) -> float:
    return float(np.cos(np.power(u, 2)))

def y_t (u: float) -> float:
    return float(np.sin(np.power(u, 2)))

def arc_length (t: float) -> float:
    """Arc length formula to integrate"""
    return float(np.sqrt(np.sin(t**2) ** 2 + np.cos(t**2) ** 2))

def plot(ax: Axes) -> None:
    # Make variable for bound of t - D. Biersach
    t_f: float = 12.34

    ts: NDArray[np.float_] = np.linspace(0, t_f, 500)
    xs = np.array(quad(x_t, 0, 0)[0]) #type: ignore
    ys = np.array(quad(y_t, 0, 0)[0]) #type: ignore

    for t in ts[1:]:
        xs = np.append(xs, quad(x_t, 0, t)[0]) # type: ignore
        ys = np.append(ys, quad(y_t, 0, t)[0]) # type: ignore

    # Calculate arc length using formula 
    length = quad(arc_length, 0, t_f)[0] #type: ignore

    # Find (x, y) for t goes to infinity - from D. Biersach
    c: float = np.sqrt(np.pi / 2) / 2
    ax.scatter(c, c, color="red")

    # Plot and label with arc length and point
    ax.plot(xs, ys)
    ax.set_title(f'Arc Length = {length:.4}')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.suptitle("Euler's Curve")
    plt.show()

if __name__ == "__main__":
    main()
