import random
import copy
import time
import os
import game

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clear():
    os.system('clear')


class Cell:
    def __init__(self, ident) -> None:
        self.is_faceup = False
        self.is_matched = False
        self.force_faceup = False
        self.ident = ident


class Grid:
    def get_unique_identifier(self, use_emoji=False):
        if use_emoji:
            i = random.randrange(len(self.emojis))
            return self.emojis.pop(i)
        else:
            print(len(self.numerics))
            i = random.randrange(len(self.numerics))
            return self.numerics.pop(i)

    def __init__(self, size, use_emoji=False) -> None:
        self.identifier = 0
        self.grid = []
        self.size = size
        self.emojis = [
            "🚀", "🌍", "🌟", "🍕", "🎉", "🐼",
            "🎸", "📚", "⚽", "🌺", "🌈", "🍔",
            "🚲", "🌻", "🎈", "🏀", "🍦", "🌳"
        ]
        self.number_of_pairs = (size * size) // 2
        self.numerics = [str(i) for i in range(self.number_of_pairs)]
        self.actual_guesses = 0
        self.minimum_possible_guesses = self.number_of_pairs
        for _ in range(self.number_of_pairs):
            cell = Cell(self.get_unique_identifier(use_emoji))
            self.grid.append(copy.copy(cell))
            self.grid.append(copy.copy(cell))
        self.shuffle()

    def shuffle(self) -> None:
        for i in range(len(self.grid)-1, 0, -1):
            j = random.randint(0, i)
            self.grid[i], self.grid[j] = self.grid[j], self.grid[i]

    def at(self, i, j) -> Cell:
        return self.grid[(i*self.size)+j]

    def index(self, i) -> Cell:
        return self.grid[i]

    def index_at(self, i, j) -> int:
        return (i*self.size)+j

    def choose(self, i, j) -> None:
        self.actual_guesses += 1
        c1 = self.grid[i]
        c2 = self.grid[j]

        c1.is_faceup = True
        c2.is_faceup = True
        clear()
        self.show()
        game.manu()
        if c1.ident == c2.ident:
            c1.is_matched = True
            c2.is_matched = True
        else:
            if not c1.is_matched:
                c1.is_faceup = False
            if not c2.is_matched:
                c2.is_faceup = False
            time.sleep(2)
        clear()
        self.show()

    def faceup(self, index) -> None:
        self.actual_guesses += 2
        self.grid[index].force_faceup = True

    def show(self, reveal=False) -> None:
        padding = 7
        print("\n"+" "*4, end='')
        for i in range(self.size):
            print(("["+alphabets[i]+"]").center(padding," "), end='')
        print('\n')

        for i in range(self.size):
            print("["+str(i)+"] ", end='')
            for j in range(self.size):
                cell = self.at(i, j)
                if cell.is_faceup or cell.is_matched or reveal or cell.force_faceup:
                    if cell.ident.isdigit():
                        print(str(cell.ident).center(padding, " "), end='')
                    else:
                        print(str(cell.ident).center(padding-1, " "), end='')
                else:
                    print("X".center(padding, " "), end='')

            print('\n')

        if self.game_over():
            score = (self.minimum_possible_guesses / self.actual_guesses) * 100
            if self.cheated():
                print("You cheated - Loser!. You're score is 0!")
            else:
                print("Oh Happy Day. You've won!! Your score is: {:.2f}".format(score))

    def game_over(self):
        revealed_cell = 0
        for c in self.grid:
            if c.is_faceup or c.force_faceup:
                revealed_cell += 1
        return revealed_cell == len(self.grid)

    def cheated(self):
        revealed_cell = 0
        for c in self.grid:
            if c.force_faceup:
                revealed_cell += 1
        return revealed_cell == len(self.grid)
