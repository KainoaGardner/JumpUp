
from display import *
from mapMaker import *
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        display()
        # mapMakerDisplay()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main()