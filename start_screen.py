import pygame
import os

# Clase startScreen de pantalla de inicio
class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = self.load_font('Opsilon-Regular.ttf', 36)  

# Método para cargar la fuente
    def load_font(self, font_name, size):
        font_path = os.path.join('assets', 'fonts', font_name)
        return pygame.font.Font(font_path, size)

 # Método para mostrar el inicio
    def display(self):
        welcome_message = "Estás en Believe & Achieve!"
        description_message = "Juego de crecimiento y superación."
        instruction_message = "Presiona la barra de espacio para continuar."

#Render de los textos
        welcome_text = self.font.render(welcome_message, True, (0, 0, 0))
        description_text = self.font.render(description_message, True, (0, 0, 0))
        instruction_text = self.font.render(instruction_message, True, (0, 0, 0))

#Render de los cuadros de texto y ubica
        welcome_rect = welcome_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 3))
        description_rect = description_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        instruction_rect = instruction_text.get_rect(center=(self.screen.get_width() // 2, (self.screen.get_height() // 3) * 2))

#Bucle
        while True:
            self.screen.fill((255, 255, 255))

#Dibuja los textos
            self.screen.blit(welcome_text, welcome_rect)
            self.screen.blit(description_text, description_rect)
            self.screen.blit(instruction_text, instruction_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
