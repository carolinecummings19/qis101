#!/usr/bin/env python3
"""connect_four.py"""

# Treyanna WilliamsTask 05-03

def who_won (brd: list[list[int]]) -> int: 
    """Return number corresponding to player """
    rows: int = len(brd)
    cols: int = len(brd[0])
    winner: int = 0

    """Checks horizontal winner generated by chatGPT"""
    for r in range(rows):
        for c in range(cols - 3):
            if brd[r][c] == brd[r][c+1] == brd[r][c+2] == brd[r][c+3] != 0:
                    winner = brd[r][c]

    """Check vertical winner"""
    for c in range(cols):
        for r in range(rows - 3):
            if brd[r][c] == brd[r+1][c] == brd[r+2][c] == brd[r+3][c] != 0:
                    winner = brd[r][c]

    """Check vertical winner """
    for c in range(cols):
        for r in range(rows - 3):
            if brd[r][c] == brd[r+1][c] == brd[r+2][c] == brd[r+3][c] != 0:
                    winner = brd[r][c]

    """Check diagonal (down) winner"""
    for r in range(rows - 3):
        for c in range(cols - 3):
            if brd[r][c] == brd[r+1][c+1] == brd[r+2][c+2] == brd[r+3][c+3] != 0:
                    winner = brd[r][c]

    """Check diagonal (up) winner"""
    for r in range(rows - 3):
        for c in range(3, cols):
            if brd[r][c] == brd[r+1][c-1] == brd[r+2][c-2] == brd[r+3][c-3] != 0:
                    winner = brd[r][c]

    return winner

def print_winner(board: list[list[int]]) -> None:
    print(*board, sep="\n")

    """Call method and print game outcome"""
    winner: int = who_won(board)
    if winner == 0:
        print("No player has won.")
    else:
        print(f"Player {winner} is the winner!")
    print()

def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)

    
    board4: list[list[int]] = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board4)

    board5: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 2, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [2, 1, 1, 2, 2, 2, 0],
    ]
    print_winner(board5)


if __name__ == "__main__":
    main()
