import pygame as pg
from settings import *
from modules import *
import sys


def draw_window(win, player1_grid, player2_grid):
    win.fill("black")

    for row in player1_grid.grid_nett:
        for block in row:
            block.draw()
    for row in player2_grid.grid_nett:
        for block in row:
            block.draw()

    pg.display.update()



def main(win):
    player1_grid = Grid("left")
    player2_grid = Grid("right")
    run = True 
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False 
                sys.exit()
        
        draw_window(win, player1_grid, player2_grid)


if __name__ == "__main__":
    main(WIN)
