import pygame
from settings import *

def getImage(sheet,width,height):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet,(0,0),(0,0,24,24))
    image = pygame.transform.scale(image,(TILESIZE,TILESIZE))
    image.set_colorkey("black")

    return image

