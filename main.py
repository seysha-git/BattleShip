import pygame as pg
from settings import *
from modules import *
import sys

def get_player_ships(player1):
    a,b = input("Where do you want to place boat with length 2 (Give me a tuple to work with): ")
    player1.place_ship(a,b,2)
    for _ in range(2):
        c,d = input("Where do you want to place boat of legnth 3 (Give me a tuple to work with): ")
        player1.place_ship(c,d,3)
    f,g = input("Where do you want to place boat with length 4 (Give me a tuple to work with): ")
    player1.place_ship(f,g,4)
    m,h = input("Where do you want to place boat with length 5 (Give me a tuple to work with): ")
    player1.place_ship(m,h,2)

def draw_window(win, player1_grid, player2_grid):
    win.fill("black")
    for row in player1_grid.grid_nett:
        for item in row:
            item.draw()
    for row in player2_grid.grid_nett:
        for item in row:
            item.draw()
    pg.display.update()



def main(win):
    player1_grid = UserGrid("left")
    player2_grid = UserGrid("right")
    run = True
    finished = False 
    #get_player_ships(player1_grid)
    finished = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False 
                sys.exit()
        
        draw_window(win, player1_grid, player2_grid)


if __name__ == "__main__":
    
    main(WIN)
