"""Simple 2D grid game prototype.

Player '@' moves with w/a/s/d. '#' are walls. 'G' is goal.
Press 'q' to quit.
"""

def main():
    grid = [
        "#####",
        "#   #",
        "# # #",
        "# G #",
        "#####",
    ]
    player = [1, 1]  # row, col
    goal = None
    for r, row in enumerate(grid):
        if 'G' in row:
            goal = [r, row.index('G')]
    moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    while True:
        # render
        for r, row in enumerate(grid):
            line = ""
            for c, ch in enumerate(row):
                if [r, c] == player:
                    line += '@'
                else:
                    line += ch
            print(line)
        cmd