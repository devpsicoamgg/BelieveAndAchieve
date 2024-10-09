import pygame
import constants
import sys

# Inicialización de PyGame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((constants.DIMENSIONS_WINDOW))
pygame.display.set_caption('Believe 🌟 & Achieve 🪜 with Kodland')



# Bucle del juego
run = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
    

