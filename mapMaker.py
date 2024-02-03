import pygame
from settings import *
from tile import *

pygame.init()
def mapMakerDisplay():
    screen.fill("#ecf0f1")
    editor.update()

class Editor():
    def __init__(self):
        self.tileGroup = pygame.sprite.Group()
        self.print = False
        self.font = pygame.font.SysFont("Bahnschrift",25)

        self.level = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]



    def place(self):
        mosPos = pygame.mouse.get_pos()
        if 0 < mosPos[0] < WIDTH and 0 < mosPos[1] < HEIGHT:
            if pygame.mouse.get_pressed()[0]:
                self.level[mosPos[1] // TILESIZE][mosPos[0] //TILESIZE] = '1'
            elif pygame.mouse.get_pressed()[2]:
                self.level[mosPos[1] // TILESIZE][mosPos[0] //TILESIZE] = '0'

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.print == False:
            for row in self.level:
                print(row,end="")
                print(",")
            self.print = True

        if key[pygame.K_SPACE] == False:
            self.print = False

    def displayTiles(self):
        for r,row in enumerate(self.level):
            for c,col in enumerate(row):
                if self.level[r][c] == '1':
                    pygame.draw.rect(screen,"#2d3436",pygame.Rect(c*TILESIZE,r*TILESIZE,TILESIZE,TILESIZE))

    def displayLines(self):
        for r in range(len(self.level)):
            pygame.draw.line(screen,"black",(0,r *TILESIZE),(WIDTH,r*TILESIZE))
            pygame.draw.line(screen, "black", (r * TILESIZE, 0), (r * TILESIZE, HEIGHT))

    def displayNumbers(self):
        for r in range(len(self.level)):
            numberText = self.font.render(f"{r + 1}",True,"Black")
            numberTextRect = numberText.get_rect(center = (r * TILESIZE + TILESIZE//2,TILESIZE//2))
            numberTextRect2 = numberText.get_rect(center=(TILESIZE // 2, r * TILESIZE + TILESIZE // 2))
            screen.blit(numberText,numberTextRect)
            screen.blit(numberText, numberTextRect2)

    def update(self):
        self.place()
        self.displayTiles()
        self.displayLines()
        self.displayNumbers()

editor = Editor()