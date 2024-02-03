import pygame

TILESIZE = 50

WIDTH = 20 * TILESIZE
HEIGHT =  20 * TILESIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

playerSpriteSheet = pygame.image.load('graphics/AnimationSheet_Character.png').convert_alpha()