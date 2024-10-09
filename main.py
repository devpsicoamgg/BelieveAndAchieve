import pygame
import sys
import constants

#Inicialización de pygame
pygame.init()

# Crea la ventana
screen = pygame.display.set_mode((constants.DIMENSIONS_WINDOW))
pygame.display.set_caption('Believe 🌟 & Achieve 🪜 with Kodland')

# Bucle  
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()