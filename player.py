import pygame
from settings import *
from map import *
from util import *
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        # self.x = x
        # self.y = y
        self.speed = 5
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        # self.image = getImage(playerSpriteSheet,32,32)
        self.image.fill("#c0392b")
        self.rect = self.image.get_rect(topleft = (x,y))
        self.gravity = .8
        self.direction = pygame.math.Vector2(0,0)

        self.jumping = False
        self.inAir = False
        self.jumpTimer = 0

        self.faceRight = False
        self.faceLeft = False

    def move(self):
        key = pygame.key.get_pressed()
        if self.inAir == False:
            if key[pygame.K_a]:
                self.direction.x = -1
                self.faceLeft = True
            if key[pygame.K_d]:
                self.direction.x = 1
                self.faceRight = True
            if key[pygame.K_SPACE]:
                self.jumping = True
                self.jumpTimer += .6
                self.speed = 0

            if key[pygame.K_a] and key[pygame.K_d]:
                self.direction.x = 0
                self.faceRight = False
                self.faceLeft = False

            if key[pygame.K_a] == False:
                self.faceLeft = False

            if key[pygame.K_d] == False:
                self.faceRight = False

            if key[pygame.K_a] == False and key[pygame.K_d] == False and self.jumping == False:
                self.direction.x = 0
                self.faceRight = False
                self.faceLeft = False

            if key[pygame.K_SPACE] == False or self.jumpTimer > 25:
                if self.jumping and self.jumpTimer > 0:
                    self.inAir = True
                    self.jump()
                self.jumping = False
                self.jumpTimer = 0
                self.speed = 5




        self.rect.x += self.direction.x * self.speed

    def jump(self):
        if self.faceRight and not self.faceLeft:
            direction = 1.7
        elif self.faceLeft and not self.faceRight:
            direction = -1.7
        else:
            direction = 0
        self.direction.x = direction
        self.direction.y = -self.jumpTimer

    def horizonatlCol(self):
        for tile in map.tileGroup.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = tile.rect.left
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right

                if self.direction.x > 0 and self.inAir:
                    self.direction.x = -self.direction.x / 2
                elif self.direction.x < 0 and self.inAir:
                    self.direction.x = -self.direction.x / 2

    def verticalCol(self):
        self.applyGravity()
        for tile in map.tileGroup.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                    self.direction.y = 0
                    self.inAir = False
                if self.direction.y < 0:
                    self.rect.top = tile.rect.bottom
                    self.direction.y = 0

    def changeLevel(self):
        if self.rect.top < 0 and self.direction.y < 0:
            self.rect.top = HEIGHT
            map.changeLevel(1)
        if self.rect.bottom > HEIGHT and self.direction.y > 0:
            self.rect.bottom = 0
            map.changeLevel(-1)


    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        if self.direction.y > 0:
            self.inAir = True

        if self.direction.y > 25:
            self.direction.y = 25

    def display(self):
        self.move()
        self.horizonatlCol()
        self.verticalCol()
        self.changeLevel()
        screen.blit(self.image,self.rect)

player = Player(WIDTH//2 - TILESIZE // 2,HEIGHT - TILESIZE * 2)