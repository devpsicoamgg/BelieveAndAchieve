import pygame
import constants

class Player(): 
    def __init__(self, x, y, animations):
        self.flip = False
        self.animations = animations
        self.index = 0
        self.image = self.animations[self.index]
        self.shape = pygame.Rect(x, y, constants.WIDTH_PLAYER, constants.HEIGHT_PLAYER)
        self.speed = constants.MOVE_SPEED 

# Vars para el cooldown de la animación
        self.animation_cooldown = constants.COOLDOWN
        self.last_update = pygame.time.get_ticks()  

    def move(self, delta_x, delta_y):
        new_x = self.shape.x + delta_x
        new_y = self.shape.y + delta_y

        # Verifica los límites de la pantalla
        if new_x < 0:
            new_x = 0  # izquierdo
        elif new_x > constants.DIMENSIONS_WINDOW[0] - constants.WIDTH_PLAYER:
            new_x = constants.DIMENSIONS_WINDOW[0] - constants.WIDTH_PLAYER  # derecho

        if new_y < 0:
            new_y = 0  # arriba
        elif new_y > constants.DIMENSIONS_WINDOW[1] - constants.HEIGHT_PLAYER:
            new_y = constants.DIMENSIONS_WINDOW[1] - constants.HEIGHT_PLAYER  # abajo

        # Actualiza posición del jugador
        self.shape.x = new_x
        self.shape.y = new_y

        # Invertir la imagen con el método flip
        if delta_x < 0:  # Mov izquierda
            self.flip = True
        elif delta_x > 0:  # Mov derecha
            self.flip = False

        # Llamamos al método para actualizar la animación
        self.update_animation(delta_x, delta_y)

    def update_animation(self, delta_x, delta_y):
        # Solo actualiza la animación si el jugador se está moviendo
        if delta_x != 0 or delta_y != 0:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update > self.animation_cooldown:
                self.last_update = current_time  
                self.index = (self.index + 1) % len(self.animations)  
                self.image = self.animations[self.index]

    def draw(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        image_x = self.shape.x + (self.shape.width - self.image.get_width()) // 2
        image_y = self.shape.y + (self.shape.height - self.image.get_height()) // 2
        interfaz.blit(image_flip, (image_x, image_y))
        # pygame.draw.rect(interfaz, constants.ORANGE, self.shape, width=1)
