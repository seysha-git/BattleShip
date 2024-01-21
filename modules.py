import pygame as pg 
import sys
from settings import *


class UserGrid:
    def __init__(self, side):
        self.side = side
        self.rows = 10
        self.columns = 10
        #self.ships = [Ship(i,i,3) for i in range(3)]
        self.grid_nett = self.create_grid()
        self.collision_nett = self.create_collision_grid()
        print(self.show_grid())
    def create_collision_grid(self):
        map = []
        for i in range(self.rows):
            col = self.columns*[False]
            map.append(col)
        return map
    def place_ship(self, length, col, row, gridnett):
         for i in range(self.rows):
            for j in range(self.columns):
                if i == row and j >= 3 and j <= col + length :
                    for n in range(length):
                        ship = Ship(length, 50 + j*75,50 + i*75*n, color="red")
                        gridnett[i][j] = ship
    def create_grid(self):
        if self.side == "left":
            gridnett = []
            for i in range(self.rows):
                col = self.columns*[0]
                gridnett.append(col)
            for i in range(self.rows):
                for j in range(self.columns):
                    block = Block(50 + j*75, 50 + i*75 )
                    gridnett[i][j] = block
                    self.place_ship(2,2,3,gridnett)
            return gridnett
        if self.side == "right":
            gridnett = []
            for i in range(self.rows):
                col = self.columns*[0]
                gridnett.append(col)
            for i in range(self.rows):
                for j in range(self.columns):
                    block = Block(WIN_WIDTH//2 + j*75, 50 + i*75 )
                    gridnett[i][j] = block 
            return gridnett

    def show_grid(self):
        for i in self.collision_nett:
            for j in i:
                print([i][j])
        print("--------------------")
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



class Ship(Block):
    def __init__(self, length, x,y,width=70, height=70, color="blue"):
        self.length = length
        super().__init__(x,y,width,height, color)
    def draw(self):
        block = pg.Rect(self.x, self.y,self.width, self.height)
        pg.draw.rect(WIN, self.color, block)
            

            



