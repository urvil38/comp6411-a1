import random
import copy
import time
import os

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Cell:
    def __init__(self, ident) -> None:
        self.is_faceup = False
        self.is_matched = False
        self.force_faceup = False
        self.ident = ident


class Grid:
    def get_unique_identifier(self) -> int:
        self.identifier += 1
        return self.identifier
    
    def __init__(self, size) -> None:
        self.identifier = 0
        self.grid = []
        self.size = size
        self.number_of_pairs = (size * size) // 2
        for _ in range(self.number_of_pairs):
            cell = Cell(self.get_unique_identifier())
            self.grid.append(copy.copy(cell))
            self.grid.append(copy.copy(cell))
        self.shuffle()

    def shuffle(self) -> None:
        for i in range(len(self.grid)-1,0,-1):
            j = random.randint(0, i)
            self.grid[i], self.grid[j] = self.grid[j], self.grid[i]

    def at(self, i, j) -> Cell:
        return self.grid[(i*self.size)+j]
    
    def index(self, i) -> Cell:
        return self.grid[i]
    
    # def get_one_and_only_faceup_cell_index(self):
    #     found = None
    #     for i in range(len(self.grid)):
    #         if self.grid[i].is_faceup:
    #             if found is None:
    #                 found = i
    #             else:
    #                 return None
    #     return found

    # def set_one_and_only_faceup_cell_index(self, index):
    #     for i in range(len(self.grid)):
    #         self.grid[i].is_faceup = (i == index)

    def index_at(self, i, j) -> int:
        return (i*self.size)+j
    
    def choose(self, i, j) -> None:
        c1 = self.grid[i]
        c2 = self.grid[j]

        c1.is_faceup = True
        c2.is_faceup = True
        os.system('clear')
        self.show()
        if c1.ident == c2.ident:
            c1.is_matched = True
            c2.is_matched = True
        else:
            c1.is_faceup = False
            c2.is_faceup = False
            time.sleep(2)
            os.system('clear')
            self.show()
           

    def faceup(self, index) -> None:
        self.grid[index].force_faceup = True 

    def show(self, reveal = False) -> None:
        print()
        print(" "*4, end='')
        for i in range(self.size):
            print("["+alphabets[i]+"]  ", end='')
        print('\n')


        for i in range(self.size):
            print("["+str(i)+"] ", end='')
            for j in range(self.size):
                cell = self.at(i, j)
                if cell.is_faceup or cell.is_matched or reveal or cell.force_faceup:
                    print(str(cell.ident).rjust(2)+"   ",end='')
                else:
                    print("X".rjust(2)+"   ", end='')
            
            print('\n')