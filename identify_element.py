#!/usr/bin/env python3
"""identify_element.py"""

# Task 17-01
# Caroline Cummings
# Plot an interpolated T vs. V curve

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

def find_molar_mass (slope: np.float_, pressure: float, mass: float) -> float:
    """Using ideal gas law, find molar mass"""
    gas_constant: float = 0.082057338
    n = (slope * pressure) / gas_constant
    molar_mass = float(mass / n)
    return molar_mass

def plot(ax: Axes) -> None:
    # Make arrays for the data in table
    temps: NDArray[np.float_] = np.array([-50, 0, 50, 100, 150])
    vols: NDArray[np.float_] = np.array([11.6, 14.0, 16.2, 19.4, 21.8])

    ax.scatter(temps, vols)

    # Linear regression
    a, b = np.polyfit(temps, vols, 1)
    ax.plot(temps, a*temps + b, color="gray") 

    # Find gas - argon(18.7)
    p = 2.00 #atm
    m = 50.0 #g
    m_mass = find_molar_mass(a, p, m)
    
    # Label plot
    ax.set_title(f'molar mass = {m_mass:.4} (Ar)')
    ax.set_xlabel(r"Temperature $(\degree K)$")
    ax.set_ylabel(r"Volume $(m^3)$")

def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.suptitle(r'  Interpolated T $(\degree K)$ vs. V $(m^3)$')
    #plt.title(r'molar mass = ')
    plt.show()

if __name__ == "__main__":
    main()
