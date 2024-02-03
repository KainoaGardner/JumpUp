import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        # self.image = image
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill("#2d3436")
        self.rect = self.image.get_rect(topleft = (x,y))

