import pygame


class WeaponOfKindness():
    def __init__(self, image, x, y):
        self.original_image = image  
        self.image = image  
        self.angle = 0  
        self.position = pygame.Vector2(x, y)  
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, player_position, player_flip):
        # Desempaqueta la posición del jugador
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_x, player_y = player_position

        # Calcula la posición del arma en función de si el jugador está mirando hacia la izquierda o derecha
        if player_flip:  # Jugador mirando hacia la izquierda
            self.position.x = player_x - 25  # Ajusta la posición a la izquierda
        else:  # Jugador mirando hacia la derecha
            self.position.x = player_x + 25  # Ajusta la posición a la derecha

        self.position.y = player_y - 5  # Mantiene la misma posición en Y
        self.rect = self.image.get_rect(center=self.position)


    def rotate(self, player_flip):
 # Rotación del arma
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        # Invertir el arma dependiendo de la dirección del jugador
        if player_flip:
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.original_image

        self.rect = self.image.get_rect(center=self.position)

    def draw(self, surface):
        # Dibuja el arma 
        surface.blit(self.image, self.rect.topleft)

    def shoot(self):
        # Disparos básicos
        print(f"Shooting the WeaponOfKindness from position {self.position} with angle {self.angle}")
