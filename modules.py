import pygame as pg 
import sys



class Grid:
    def __init__(self):
        self.rows = 10
        self.columns = 10
        self.grid = self.create_grid()
    def create_grid(self):
        gridnett = []
        for i in range(self.rows):
            col = self.columns*[0]
            gridnett.append(col)
        return gridnett
    def show_grid(self):
        for i in self.grid:
            print(i)


class Block:
    ...







class Player1Grid(Grid):
    ...
class Player2Grid(Grid):
    ...



class Ship:
    ...
