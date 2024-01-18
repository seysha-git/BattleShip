import pygame as pg 
import sys
from settings import *


class Grid:
    def __init__(self, side):
        self.side = side
        self.rows = 10
        self.columns = 10
        self.grid_nett = self.create_grid()
    def create_grid(self):
        if self.side == "left":
            gridnett = []
            for i in range(self.rows):
                col = self.columns*[0]
                gridnett.append(col)
            for i in range(self.rows):
                for j in range(self.columns):
                    block = Block(50 + j*80, 50 + i*80 )
                    gridnett[i][j] = block 
            return gridnett
        if self.side == "right":
            gridnett = []
            for i in range(self.rows):
                col = self.columns*[0]
                gridnett.append(col)
            for i in range(self.rows):
                for j in range(self.columns):
                    block = Block(WIN_WIDTH//2 + j*80, 50 + i*80 )
                    gridnett[i][j] = block 
            return gridnett

    def show_grid(self):
        for i in self.grid_nett:
            for j in i:
                print(j.x, j.y)
                print("----------")


class Block:
    def __init__(self, x,y,width=70, height=70, color="white"):
        self.x = x
        self.y = y 
        self.width = width 
        self.height = height
        self.color = color 
    def draw(self):
        block = pg.Rect(self.x, self.y,self.width, self.height)
        pg.draw.rect(WIN, self.color, block)



class Player1Grid(Grid):
    ...
class Player2Grid(Grid):
    ...



class Ship:
    ...
