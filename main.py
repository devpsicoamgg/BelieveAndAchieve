import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Believe & Achieve')


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    screen.fill(WHITE)
    

    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100))
    

    pygame.display.flip()
