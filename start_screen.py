import pygame
import os

# Clase StartScreen de pantalla de inicio
class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = self.load_font('Opsilon-Regular.ttf', 36)
        self.options = ["Iniciar Juego", "Instrucciones", "Salir"]
        self.selected_option = 0

    # Método para cargar la fuente
    def load_font(self, font_name, size):
        font_path = os.path.join('assets', 'fonts', font_name)
        return pygame.font.Font(font_path, size)

    # Método para mostrar el inicio
    def display(self):
        while True:
            self.screen.fill((255, 255, 255))

            # Mensaje de bienvenida
            welcome_message = "Estás en Believe & Achieve!"
            welcome_text = self.font.render(welcome_message, True, (0, 0, 0))
            welcome_rect = welcome_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 4))
            self.screen.blit(welcome_text, welcome_rect)

            # Mostrar opciones de menú
            for i, option in enumerate(self.options):
                color = (0, 0, 0) if i != self.selected_option else (255, 0, 0)  # Resalta la opción seleccionada
                option_text = self.font.render(option, True, color)
                option_rect = option_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + i * 40))
                self.screen.blit(option_text, option_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:  # Iniciar Juego
                            return "start_game"
                        elif self.selected_option == 1:  # Instrucciones
                            self.show_instructions()
                        elif self.selected_option == 2:  # Salir
                            pygame.quit()
                            exit()

    # Método para mostrar instrucciones
    def show_instructions(self):
        instructions = [
            "Usa W, A, S, D para moverte y",
            "la barra espaciadora para disparar.",
            "Usa ESC para regresar."
        ]
        
        self.screen.fill((255, 255, 255))
        
        # Renderizar e imprimir cada línea de instrucciones
        for i, line in enumerate(instructions):
            instruction_text = self.font.render(line, True, (0, 0, 0))
            instruction_rect = instruction_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + i * 40))
            self.screen.blit(instruction_text, instruction_rect)

        pygame.display.flip()

        # Espera a que el usuario presione una tecla para regresar al menú
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
