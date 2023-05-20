import grid
import sys
import os
from typing import Tuple

banner = """
----------------------
|     PEEK-A-BOO     |
----------------------
"""
def clear():
    os.system('clear')

def manu():
    str = """
1. Let me select two elements
2. Uncover one element for me
3. I give up - reveal the grid
4. New game
5. Exit"""
    print(str)

def input_and_validate_coordinate(size) -> Tuple[int, int]:
    while True:
        co = input("Enter cell coordinates (e.g., a0): ").strip()
        if len(co) > 1:
            col = co[0].upper()
            row = co[1:]
            if col.isalpha():
                j = grid.alphabets.index(col)
                if j > size-1:
                    print("Input error: column entry is out of range for this grid. Please try again.")
                    continue
                elif j < 0:
                    print("Invalid coordinate. Please try again.")
                    continue

            try:
                i = int(row)
                if i > size-1:
                    print("Input error: row entry is out of range for this grid. Please try again.")
                    continue
            except:
                print("Invalid coordinate. Please try again.")
                continue
            
            return (i, j)
        else:
            print("Invalid coordinate. Please try again.")


def choose_one_element(size) -> Tuple[int, int]:
    return input_and_validate_coordinate(size)
    

def game_loop():
    print(banner)
    g = grid.Grid(grid_size)
    g.show()
    while True:
        manu()
        try:
            selected = int(input("\nSelect: "))
            if selected == 1:
                c1 = choose_one_element(g.size)
                c2 = choose_one_element(g.size)
                g.choose(g.index_at(c1[0], c1[1]), g.index_at(c2[0], c2[1]))
            elif selected == 2:
                co = choose_one_element(g.size)
                g.faceup(g.index_at(co[0], co[1]))
                clear()
                g.show()
            elif selected == 3:
                clear()
                g.show(reveal=True)
            elif selected == 4:
                g = grid.Grid(grid_size)
                clear()
                g.show()
            elif selected == 5:
                break
        except ValueError:
            print("Invalid Option")

if __name__ == "__main__":
    grid_size = 2

    if len(sys.argv) > 1:
        try:
            grid_size = int(sys.argv[1])
        except ValueError:
            print("Please provide valid grid size. must be 2, 4 or 6.")
            exit(0)

        if grid_size not in [2,4,6]:
            print("Invalid grid size provided. must be 2, 4 or 6.")
            exit(0)

    game_loop()