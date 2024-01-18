import pygame as pg 
import sys
from settings import *


class Grid:
    def __init__(self):
        self.rows = 10
        self.columns = 10
        self.grid_nett = self.create_grid()
    def create_grid(self):
        gridnett = []
        for i in range(self.rows):
            block = Block(100*i,0)
            col = self.columns*[block]
            gridnett.append(col)
        return gridnett
    def show_grid(self):
        for i in self.grid_nett:
            for j in i:
                print(j.x, j.y)
                print("----------")


class Block:
    def __init__(self, x,y,width=50, height=100, color="white"):
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height
        self.color = color 
    def draw(self):
        block = pg.Rect(self.x, self.y,self.width, self.height)
        pg.draw.rect(WIN, self.color, block)



grid = Grid()

print(grid.show_grid())



class Player1Grid(Grid):
    ...
class Player2Grid(Grid):
    ...



class Ship:
    ...
