import pygame
import constants

class Player(): 
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, constants.WIDTH_PLAYER, constants.HEIGHT_PLAYER)
        self.shape.center = (x, y)
        self.speed = constants.MOVE_SPEED 

# Calcula posición con cada movimiento
    def move(self, delta_x, delta_y):
        new_x = self.shape.x + delta_x
        new_y = self.shape.y + delta_y
        
# Verifica los límites de la pantalla
        if new_x < 0:
            new_x = 0  # izquierdo
        if new_x + self.shape.width > constants.DIMENSIONS_WINDOW[0]:
            new_x = constants.DIMENSIONS_WINDOW[0] - self.shape.width  # derecho
        if new_y < 0:
            new_y = 0  # arriba
        if new_y + self.shape.height > constants.DIMENSIONS_WINDOW[1]:
            new_y = constants.DIMENSIONS_WINDOW[1] - self.shape.height  # abajo

# Actualiza la posición del jugador
        self.shape.x = new_x
        self.shape.y = new_y

    def draw(self, interfaz):
        pygame.draw.rect(interfaz, constants.ORANGE, self.shape)