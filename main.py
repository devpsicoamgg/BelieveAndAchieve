import pygame
import constants
import sys
from player import Player
from start_screen import StartScreen
from weaponsOfKindness import WeaponOfKindness
import os

# Inicialización de PyGame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode(constants.DIMENSIONS_WINDOW)
pygame.display.set_caption('Believe 🌟 & Achieve 🪜 with Kodland')

#**************Sprites***************
# Función para escalar imágenes
def scaled_img(image, scale):
    return pygame.transform.scale(image, (int(image.get_size()[0] * scale), 
                                           int(image.get_size()[1] * scale)))

# Función para contar elementos
def count_elements(dir):
    return len(os.listdir(dir))

# Función para listar nombres de carpetas
def name_folder(dir):
    return os.listdir(dir)

# Definición del directorio de enemigos
dir_enemies = "assets/images/characters/enemies"
kind_enemies = name_folder(dir_enemies)

# Lista para almacenar las animaciones de los enemigos
animation_enemies = []

# Recorremos cada tipo de enemigo en el directorio de enemigos
for enemy_type in kind_enemies:
    enemy_path = os.path.join(dir_enemies, enemy_type)
    enemy_animations = []

    # Cuenta el número de imágenes según cada directorio
    num_images = count_elements(enemy_path)

    # Recorre cada imagen de animación del enemigo
    for i in range(num_images):  
        enemy_image_path = os.path.join(enemy_path, f'{enemy_type}_{i}.png')
        if os.path.exists(enemy_image_path):
            img = pygame.image.load(enemy_image_path).convert_alpha()
            img_scaled = scaled_img(img, constants.SCALE_ENEMY)
            enemy_animations.append(img_scaled)

    # Agregar animaciones del enemigo a la lista principal
    animation_enemies.append(enemy_animations)

# Lista para almacenar las animaciones del jugador
animations = []

# Carga y escala las imágenes del jugador
for i in range(count_elements('assets/images/characters/player')):
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

# Bucle principal del juego
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
        weapon.update(player.shape.center, player.flip)  # Actualizado a solo 3 parámetros
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
                if event.key == pygame.K_SPACE:
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
