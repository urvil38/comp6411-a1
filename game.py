import grid
import sys
from typing import Tuple

banner = """
----------------------
|     PEEK-A-BOO     |
----------------------
"""


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

            if not col.isalpha():
                print("Error: Invalid coordinate. Please try again.")
                continue

            if not row.isdigit():
                print("Error: Invalid coordinate. Please try again.")
                continue

            j = grid.alphabets.index(col)
            if j > size-1:
                print("Error: column entry is out of range for this grid. Please try again.")
                continue
            elif j < 0:
                print("Error: Invalid coordinate. Please try again.")
                continue

            try:
                i = int(row)
                if i > size-1:
                    print("Error: row entry is out of range for this grid. Please try again.")
                    continue
            except:
                print("Error: Invalid coordinate. Please try again.")
                continue

            return (i, j)
        else:
            print("Error: Invalid coordinate. Please try again.")


class Game:
    def __init__(self) -> None:
        self.grid_size = self.get_grid_size()
        self.use_emojis = self.should_use_emojis()
        self.g = grid.Grid(self.grid_size, self.use_emojis)

    def get_grid_size(self):
        if len(sys.argv) > 1:
            try:
                gsize = int(sys.argv[1])
            except ValueError:
                print("Error: Please provide valid grid size. must be 2, 4 or 6.")
                exit(0)

            if gsize not in [2, 4, 6]:
                print("Error: Invalid grid size provided. must be 2, 4 or 6.")
                exit(0)
        else:
            print("Error: Invalid execution.\nusage: python3 game.py <grid_size> [emojis]")
            exit(0)
        return gsize

    def should_use_emojis(self):
        if len(sys.argv) > 2:
            if sys.argv[2] == "emojis":
                return True
        return False

    def choose_one_element(self) -> Tuple[int, int]:
        return input_and_validate_coordinate(self.grid_size)

    def handle_option_1(self):
        while True:
            c1 = self.choose_one_element()
            c2 = self.choose_one_element()
            if c1 == c2:
                print("Error: You've selected the same cells. Please select different cells.")
                continue
            else:
                break
        self.g.choose(self.g.index_at(c1[0], c1[1]), self.g.index_at(c2[0], c2[1]))
        return True

    def handle_option_2(self):
        co = self.choose_one_element()
        self.g.faceup(self.g.index_at(co[0], co[1]))
        grid.clear()
        self.g.show()

    def handle_option_3(self):
        grid.clear()
        self.g.show(reveal=True)

    def handle_option_4(self):
        self.g = grid.Grid(self.grid_size, self.use_emojis)
        grid.clear()
        self.g.show()

    def loop(self):
        grid.clear()
        print(banner)
        self.g.show()
        while True:
            manu()
            try:
                selected = int(input("\nSelect: "))
                if selected == 1:
                    if not self.handle_option_1():
                        continue
                elif selected == 2:
                    self.handle_option_2()
                elif selected == 3:
                    self.handle_option_3()
                elif selected == 4:
                    self.handle_option_4()
                elif selected == 5:
                    break
            except ValueError:
                print("Invalid Option")


if __name__ == "__main__":
    game = Game()
    game.loop()
