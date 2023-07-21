#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

# Task 15-02
# Caroline Cummings

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def f(x: NDArray[np.float_], y: NDArray[np.float_]) -> NDArray[np.complex_]:
    """Returns complex sine function - from D. Biersach"""
    return np.array(np.abs(np.sin(x + 1j * y)))

def plot(ax: Axes) -> None:
    """Plot surface in C given by f(z) = |sinz| over [+_ 2.5 +- i]"""
    
    # From plot3d_surface.py with changed bounds - D. Biersach
    x: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    y: NDArray[np.float_] = np.linspace(-1, 1, 100)

    x, y = np.meshgrid(x, y)

    z: NDArray[np.complex_] = f(x, y)

    ax.set_title(r"Complex Sine Function: $f(z) = |sin(z)|$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    # From plot3d_surface.py
    surface = ax.plot_surface(  # type: ignore
        x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False  # type: ignore
    )
    plt.colorbar(surface, ax=ax, shrink=0.5, aspect=5)

def main() -> None: 
    # From plot3d_surface.py
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()

if __name__ == "__main__":
    main()


#score 4