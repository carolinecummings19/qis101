#!/usr/bin/env python3
"""ifs_hexagonal.py"""

# Task 19-01
# Caroline Cummings
# Code copied from ifs_triangle.py - D. Biersach

from ifs import IteratedFunctionSystem
from pygame import Color #type: ignore
from simple_screen import SimpleScreen
from math import sqrt

ifs = IteratedFunctionSystem()


def plot_ifs(ss: SimpleScreen) -> None:
    iterations = 200_000
    x: float = 0.0
    y: float = 0.0
    color: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, color = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main() -> None:
    # Specify how big image is
    ifs.set_base_frame(0, 0, 30, 30)

    # Equal probability
    p: float = 1 / 6

    # Coordinates found from drawing
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + sqrt(75), Color("blue"), p)
    ifs.add_mapping(20, 15 + sqrt(75), 15, 15, 10, 15 + sqrt(75), Color("blue"), p)
    ifs.add_mapping(10, 15 + sqrt(75), 15, 15, 5, 15, Color("blue"), p)
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - sqrt(75), Color("blue"), p)
    ifs.add_mapping(10, 15 - sqrt(75), 15, 15, 20, 15 - sqrt(75), Color("blue"), p)
    ifs.add_mapping(20, 15 - sqrt(75), 15, 15, 25, 15, Color("blue"), p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Hexagon",
    )
    ss.show()


if __name__ == "__main__":
    main()
