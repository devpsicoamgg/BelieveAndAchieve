import pygame
import constants
import sys
from player import Player
from start_screen import StartScreen  # Importar la clase StartScreen

# Inicialización de PyGame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((constants.DIMENSIONS_WINDOW))
pygame.display.set_caption('Believe 🌟 & Achieve 🪜 with Kodland')

# Creación del jugador
player = Player(x=50, y=50)

#Bucle
def main_game():
    run = True
    while run:  
        screen.fill((255, 255, 255))  

        player.draw(screen)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()  

    pygame.quit()
    sys.exit()

# Instancia de la clase StartScreen o pantalla inicio
start_screen = StartScreen(screen)

# Muestra la pantalla de inicio
start_screen.display()

# Iniciar el juego principal
main_game()
