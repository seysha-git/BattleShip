import pygame as pg
from settings import *
import sys





def main(WIN):
    run = True 
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False 
                sys.exit()
       


if __name__ == "__main__":
    main(WIN)
