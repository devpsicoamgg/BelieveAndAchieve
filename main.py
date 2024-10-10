import pygame
import constants
import sys
from player import Player
from start_screen import StartScreen
from weaponsOfKindness import WeaponOfKindness

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

# Carga y escala las imágenes del jugador
animations = []
for i in range(7):
    img = pygame.image.load(f'assets/images/characters/player/Player_{i}.png').convert_alpha()
    img_scaled = scaled_img(img, constants.SCALE_PLAYER)  
    animations.append(img_scaled)  

# Creación del jugador
player = Player(x=50, y=50, animations=animations)  

# Carga y escala la imagen del arma
weapon_image = pygame.image.load('assets/images/weaponsOfKindness/WeaponOfKindness.png').convert_alpha()
weapon_image_scaled = scaled_img(weapon_image, constants.SCALE_WEAPON)

# Carga y escala la imagen de la bala
bullet_image = pygame.image.load('assets/images/weaponsOfKindness/Bullet.png').convert_alpha()
bullet_image_scaled = scaled_img(bullet_image, constants.SCALE_BULLET)

# Instancia la clase para armas, incluyendo la imagen de la bala
weapon = WeaponOfKindness(image=weapon_image_scaled, x=player.shape.centerx, y=player.shape.centery, bullet_img=bullet_image_scaled)

# Bucle y f() general del juego
def main_game():
    # Definición de variables para el movimiento del jugador.
    move_up = False
    move_down = False
    move_left = False
    move_right = False

    # Velocidad del FPS
    clock = pygame.time.Clock()
    
    run = True
    while run:  
        clock.tick(constants.FPS)

        screen.fill(constants.BG_COLOR)  

        player.draw(screen)  

        mouse_x, mouse_y = pygame.mouse.get_pos()
        weapon.update(player.shape.center, player.flip)
        angle = (pygame.math.Vector2(mouse_x - weapon.position.x, mouse_y - weapon.position.y)).angle_to((1, 0))  # Calcula el ángulo hacia el ratón
        weapon.rotate(angle, player.flip)  # Rota el arma según el ángulo
        weapon.draw(screen)  

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

                # Detectar la tecla de disparo (barra espaciadora)
                if event.key == pygame.K_SPACE:  # Cambia esto si deseas usar otra tecla
                    weapon.shoot()  # Llama al método shoot para mostrar el mensaje

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

