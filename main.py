import pygame

from menu_nim import Menu

if __name__ == "__main__":
    
    pygame.display.init()
    pygame.font.init()
    pygame.mixer.init()

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h

    screen = pygame.display.set_mode((width, height))
    screen.fill("#175690")
    
    pygame.display.set_caption("WizardNim")

    Menu(screen).menu()