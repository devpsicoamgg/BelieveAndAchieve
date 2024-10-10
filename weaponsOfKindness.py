import pygame
import constants

class WeaponOfKindness:
    def __init__(self, image, x, y, bullet_img):
        self.original_image = image  
        self.image = self.original_image  
        self.angle = 0  
        self.position = pygame.Vector2(x, y)  
        self.rect = self.image.get_rect(center=(x, y))
        self.bullet_img = bullet_img  
        self.bullets = pygame.sprite.Group()  # Grupo para almacenar las balas

        # Define la dirección inicial
        self.direction = pygame.math.Vector2(1, 0)  # Dirección inicial a la derecha

    def update(self, player_position, player_flip):
        # Desempaqueta la posición del jugador
        player_x, player_y = player_position

        # Calcula la posición del arma en función de si el jugador está mirando hacia la izquierda o derecha
        if player_flip:  # Jugador mirando hacia la izquierda
            self.position.x = player_x - 25  # Ajusta la posición a la izquierda
        else:  # Jugador mirando hacia la derecha
            self.position.x = player_x + 25  # Ajusta la posición a la derecha

        self.position.y = player_y - 5  # Mantiene la misma posición en Y
        self.rect = self.image.get_rect(center=self.position)

        # Actualiza las balas
        self.bullets.update()

    def rotate(self, angle, player_flip):
        # Actualiza el ángulo del arma
        self.angle = angle

        # Rotación del arma
        self.image = pygame.transform.rotate(self.original_image, -self.angle)

        # Invertir el arma dependiendo de la dirección del jugador
        if player_flip:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(center=self.position)

        # dirección de la bala según ángulo
        self.direction = pygame.math.Vector2(1, 0).rotate(-self.angle)

    def shoot(self):
        # Crea una nueva bala y la agrega al grupo de balas
        bullet_x = self.position.x + self.direction.x * 5  # Ajusta el desplazamiento para que salga del cañón
        bullet_y = self.position.y + self.direction.y * 5  # Ajusta el desplazamiento para que salga del cañón
        bullet = Bullet(self.bullet_img, bullet_x, bullet_y, -self.angle)  # Usar -self.angle para que la bala mantenga la rotación correcta
        self.bullets.add(bullet)
        #print(f"Disparo ddel arma {self.position} en ángulo {self.angle}")

    def draw(self, surface):
        # Dibuja el arma 
        surface.blit(self.image, self.rect.topleft)

        # Dibuja todas las balas
        self.bullets.draw(surface)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(x, y))
        
        # Velocidad de la bala
        self.speed = constants.BULLET_SPEED
        # Dirección de la bala
        self.direction = pygame.math.Vector2(1, 0).rotate(-self.angle)  # ROTACIONES SEGUN EL ANGULO DEL ARMA

    def update(self):
        # Mueve la bala en la dirección determinada
        self.rect.topleft += self.direction * self.speed

        # Destruir la bala si sale de la pantalla
        if self.rect.bottom < 0 or self.rect.top > constants.DIMENSIONS_WINDOW[1] or \
           self.rect.right < 0 or self.rect.left > constants.DIMENSIONS_WINDOW[0]:
            self.kill()  # Elimina la bala del grupo

