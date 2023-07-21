#!/usr/bin/env python3
"""board_encoding.py"""

# Caroline Cummings - Task 07-02
# Decode a given integer representation of Tic-Tac-Toe board

from __future__ import annotations

import typing
import matplotlib.pyplot as plt

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

def decode_boardInt(num: int) -> list[int]:
    """Returns list of board numbers from integer representation"""
    
    # Define list of 0's for the 9 squares (empty board)
    squares: list[int] = [0] * 9
    n: int = num

    # Populate list with values
    for i in range(len(squares)):
        if n % 3 != 0:
            squares[i] = n % 3
        n = int(n / 3)

    return squares

def print_board (int_num: int, values: list[int]) -> None:
    """Prints board in terminal"""
    print(f"Board Number: {int_num}")
    if len(values) == 9:
        print(values[:3])
        print(values[3:6])
        print(values[6:])
    else:
        print("Invalid Board")
    print()

# Create a blank tic-tac-toe grid - from chatGPT
def create_tic_tac_toe_grid(ax: Axes, num: int, board: list[int]) -> None:
    """Prints board using matplotlib"""
    # Set up the figure and axes
    ax.set_aspect('equal')

    # Draw horizontal lines
    ax.plot([0, 3], [1, 1], 'k-', linewidth=2)
    ax.plot([0, 3], [2, 2], 'k-', linewidth=2)

    # Draw vertical lines
    ax.plot([1, 1], [0, 3], 'k-', linewidth=2)
    ax.plot([2, 2], [0, 3], 'k-', linewidth=2)

    # Remove ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Set the axis limits
    ax.set_xlim([0, 3]) # type: ignore
    ax.set_ylim([0, 3]) # type: ignore

    """Everything below is from Caroline Cummings"""
    ax.set_title(f"Board Number: {num}", size=10)

    # Fill grid
    index: int = 0
    if len(board) == 9:
        for i in range(3):
            for j in range(3):
                if board[index] == 1:
                    ax.text(0.25 + j, 2.25 - i, "X", size=25)
                if board[index] == 2: 
                    ax.text(0.25 + j, 2.25 - i, "O", size=25) 
                index += 1


def main() -> None:
    # Boards to decode
    num1, num2, num3 = 2271, 1638, 12065

    # Create lists of board values
    board1: list[int] = decode_boardInt(num1)
    board2: list[int] = decode_boardInt(num2)
    board3: list[int] = decode_boardInt(num3)
    
    # Print boards in terminal
    print_board(num1, board1)
    print_board(num2, board2)
    print_board(num3, board3)
    
    # Print boards in matplotlib
    plt.figure(__file__)

    create_tic_tac_toe_grid(plt.subplot(131), num1, board1)
    create_tic_tac_toe_grid(plt.subplot(132), num2, board2)
    create_tic_tac_toe_grid(plt.subplot(133), num3, board3)

    # Display the grids
    plt.show()
    

if __name__ == "__main__":
    main()




#Additionl comments
'''well done with the Matplotlib graphs!'''
'''Score 5'''