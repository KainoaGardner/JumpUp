import pygame
from levels import *
from settings import *
from tile import *

class Map():
    def __init__(self):
        self.levelCount = 5
        self.level = levels[self.levelCount]
        self.tileGroup = pygame.sprite.Group()
        self.createLevel()

    def createLevel(self):
        for r,row in enumerate(self.level):
            for c,col in enumerate(row):
                if self.level[r][c] == '1':
                    self.tileGroup.add(Tile(c * TILESIZE,r * TILESIZE,2))

    def changeLevel(self,amount):
        self.levelCount += amount
        self.level = levels[self.levelCount]
        self.tileGroup.empty()
        self.createLevel()

    def display(self):
        self.tileGroup.draw(screen)

map = Map()