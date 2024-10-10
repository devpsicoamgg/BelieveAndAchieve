import pygame
import constants
import sys
from player import Player
from start_screen import StartScreen

# Inicialización de PyGame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((constants.DIMENSIONS_WINDOW))
pygame.display.set_caption('Believe 🌟 & Achieve 🪜 with Kodland')

# Creación del jugador
player = Player(x=50, y=50)

#Bucle y f() general del juego
def main_game():

# Definición de variables para el movimiento del player.
    move_up = False
    move_down = False
    move_left = False
    move_right = False

# velocidad del FPS
    clock = pygame.time.Clock()
    
    
    run = True
    while run:  
        
        clock.tick(constants.FPS)

        screen.fill(constants.BG_COLOR)  

        player.draw(screen)  

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False


# Detecta cuando las tecla de movimiento son presionadas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up = True
                    print('Se movió hacia arriba')
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down = True
                    print('Se movió hacia abajo')
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left = True
                    print('Se movió a la izquierda')
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right = True
                    print('Se movió a la derecha')

# Detectar cuando una tecla es soltada para retornar a false el movimiento
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right = False

# Movimiento del player según las variables. 
        delta_x = 0
        delta_y = 0
        if move_up:
            delta_y = -player.speed
        if move_down:
            delta_y = player.speed
        if move_left:
            delta_x = -player.speed
        if move_right:
            delta_x = player.speed

        player.move(delta_x, delta_y)



        pygame.display.flip()  

    pygame.quit()
    sys.exit()

# Instancia de la clase StartScreen o pantalla inicio
start_screen = StartScreen(screen)

# Muestra la pantalla de inicio
start_screen.display()

# Iniciar el juego principal
main_game()
