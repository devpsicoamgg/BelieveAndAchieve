import pygame
import constants

class Player(): 
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, constants.WIDTH_PLAYER, constants.HEIGHT_PLAYER)
        self.shape.center = (x, y)

    def draw(self, interfaz):
        pygame.draw.rect(interfaz, constants.ORANGE, self.shape)
