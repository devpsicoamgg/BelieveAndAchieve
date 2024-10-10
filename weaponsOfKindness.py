import pygame
import math

class WeaponOfKindness():
    def __init__(self, image, x, y):
        self.original_image = image  
        self.image = image  
        self.angle = 0  
        self.position = pygame.Vector2(x, y)  
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, player_position):
        # Centra el arma en el personaje
        self.position = pygame.Vector2(player_position)
        self.position.x += 30  
        self.position.y -= 10  
        self.rect = self.image.get_rect(center=self.position)

    def rotate(self, target_x, target_y):
        # Cálculo del arma y el target con trigonometría
        self.angle = 0 

        # Rotación del arma
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        # invertir
        if target_x < self.position.x:
            self.image = pygame.transform.flip(self.image, True, False)  
        
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, surface):
        # Dibuja el arma 
        surface.blit(self.image, self.rect.topleft)

    def shoot(self):
        # Disparos básicos
        print(f"Shooting the WeaponOfKindness from position {self.position} with angle {self.angle}")
