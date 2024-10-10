import pygame
import constants
import sys
from player import Player
from start_screen import StartScreen

# Inicialización de PyGame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode(constants.DIMENSIONS_WINDOW)
pygame.display.set_caption('Believe 🌟 & Achieve 🪜 with Kodland')

#**************Sprites***************
# f() para escalar imágenes
def scaled_img(image, scale):
    return pygame.transform.scale(image, (int(image.get_size()[0] * scale), 
                                           int(image.get_size()[1] * scale)))

# Carga y escala las imágenes
animations = []
for i in range(7):
    img = pygame.image.load(f'assets/images/characters/player/Player_{i}.png')
    img_scaled = scaled_img(img, constants.SCALE_PLAYER)  
    animations.append(img_scaled)  

# Creación del jugador
player = Player(x=50, y=50, animations=animations)  

# Bucle y f() general del juego
def main_game():
    # Definición de variables para el movimiento del jugador.
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

            # Detecta cuando las teclas de movimiento son presionadas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right = True

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

        # Movimiento del jugador según las variables. 
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

# Instancia de la clase StartScreen o pantalla de inicio
start_screen = StartScreen(screen)

# Muestra la pantalla de inicio
start_screen.display()

# Iniciar el juego principal
main_game()
