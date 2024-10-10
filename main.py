import pygame
import constants
import sys
import os
import random
from player import Player
from start_screen import StartScreen
from weaponsOfKindness import WeaponOfKindness

pygame.init()
screen = pygame.display.set_mode(constants.DIMENSIONS_WINDOW)
pygame.display.set_caption('Believe 🌟 & Achieve 🪜 with Kodland')

def scaled_img(image, scale):
    return pygame.transform.scale(image, (int(image.get_size()[0] * scale), 
                                           int(image.get_size()[1] * scale)))

def count_elements(dir):
    return len(os.listdir(dir))

def name_folder(dir):
    return os.listdir(dir)

dir_enemies = "assets/images/characters/enemies"
kind_enemies = name_folder(dir_enemies)

animation_enemies = []

for enemy_type in kind_enemies:
    enemy_path = os.path.join(dir_enemies, enemy_type)
    enemy_animations = []
    num_images = count_elements(enemy_path)

    for i in range(num_images):  
        enemy_image_path = os.path.join(enemy_path, f'{enemy_type}_{i}.png')
        if os.path.exists(enemy_image_path):
            img = pygame.image.load(enemy_image_path).convert_alpha()
            img_scaled = scaled_img(img, constants.SCALE_ENEMY)
            enemy_animations.append(img_scaled)

    animation_enemies.append(enemy_animations)

animations = []

for i in range(count_elements('assets/images/characters/player')):
    img = pygame.image.load(f'assets/images/characters/player/Player_{i}.png').convert_alpha()
    img_scaled = scaled_img(img, constants.SCALE_PLAYER)  
    animations.append(img_scaled)  

player = Player(x=50, y=50, animations=animations)  

weapon_image = pygame.image.load('assets/images/weaponsOfKindness/WeaponOfKindness.png').convert_alpha()
weapon_image_scaled = scaled_img(weapon_image, constants.SCALE_WEAPON)

bullet_image = pygame.image.load('assets/images/weaponsOfKindness/Bullet.png').convert_alpha()
bullet_image_scaled = scaled_img(bullet_image, constants.SCALE_BULLET)

weapon = WeaponOfKindness(image=weapon_image_scaled, x=player.shape.centerx, y=player.shape.centery, bullet_img=bullet_image_scaled)

class Enemy:
    def __init__(self, x, y, animations, situation):
        self.x = x
        self.y = y
        self.animations = animations
        self.frame_index = 0
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = 2
        self.situation = situation  # Nueva propiedad para la situación

    def update(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = self.animations[int(self.frame_index)]
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # Dibujar el texto debajo del enemigo
        font = pygame.font.Font(None, 28)
        text_surface = font.render(self.situation, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 15))
        screen.blit(text_surface, text_rect)

    def move(self):
        self.y += self.speed
        if self.y > constants.DIMENSIONS_WINDOW[1]:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, constants.DIMENSIONS_WINDOW[0] - self.rect.width)

def create_enemy():
    situations = [
    "Ansiedad",
    "Depresión",
    "No creer en sí mismo",
    "Baja autoestima",
    "Miedo al fracaso",
    "Estrés crónico",
    "Dificultades en las relaciones",
    "Sensación de soledad",
    "Perfeccionismo",
    "Falta de motivación",
    "Dudas sobre el futuro",
    "Comparación con los demás",
]
    return Enemy(random.randint(0, constants.DIMENSIONS_WINDOW[0]), random.randint(-100, -40), random.choice(animation_enemies), random.choice(situations))

enemies = []

def main_game():
    global enemies
    enemies_killed = 0
    enemy_spawn_timer = 0
    enemy_spawn_interval = 1000
    clock = pygame.time.Clock()

    run = True
    while run:  
        clock.tick(constants.FPS)
        screen.fill(constants.BG_COLOR)  

        player.draw(screen)  

        mouse_x, mouse_y = pygame.mouse.get_pos()
        weapon.update(player.shape.center, player.flip)  
        
        player_x, player_y = player.shape.center
        angle = pygame.math.Vector2(mouse_x - player_x, mouse_y - player_y).angle_to((1, 0))
        angle = max(-65, min(angle, 65))
        
        weapon.rotate(angle, player.flip)
        weapon.draw(screen)  

        for enemy in enemies:
            enemy.move()
            enemy.update()
            enemy.draw(screen)

            for bullet in weapon.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemies.remove(enemy)
                    weapon.bullets.remove(bullet)
                    enemies_killed += 1
                    break  

        font = pygame.font.Font(None, 36)
        text_surface = font.render(f'Obstáculos superados: {enemies_killed}', True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    weapon.shoot(player.flip)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            player.move(5, 0)
        if keys[pygame.K_UP]:
            player.move(0, -5)
        if keys[pygame.K_DOWN]:
            player.move(0, 5)

        enemy_spawn_timer += clock.get_time()
        if enemy_spawn_timer >= enemy_spawn_interval:
            enemies.append(create_enemy())
            enemy_spawn_timer = 0

        pygame.display.flip()  

    pygame.quit()
    sys.exit()

start_screen = StartScreen(screen)
start_screen.display()
main_game()
