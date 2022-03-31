import pygame
from pygame.locals import *

import time

from login_page import LoginPage

class Menu:

    def __init__(self, screen):

        self.screen = screen
        self.screen.fill("#175690")
        
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        self.clock = pygame.time.Clock()
        
    def menu(self):
    
        pygame.mixer.music.load("musics/music_menu.wav")
        pygame.mixer.music.play(-1)

        character1 = pygame.transform.scale(pygame.image.load("images/wizard1-final.png").convert_alpha(), (int(self.width//3.8), int(self.height//1.3)))
        character2 = pygame.transform.scale(pygame.image.load("images/wizard2-flip.png").convert_alpha(), (int(self.width//3.8), int(self.height//1.3)))
        exp = pygame.transform.scale(pygame.image.load("images/explosion.png").convert_alpha(), (int(self.width//1.44), int(self.height//0.9)))
        rules = pygame.transform.scale(pygame.image.load("images/book.png").convert_alpha(), (int(self.width//12), int(self.height//7.4)))

        character_rect1 = character1.get_rect()
        character_rect1.topleft = (self.width//27, self.height//6.7)
        character_rect2 = character2.get_rect()
        character_rect2.topleft = (self.width//1.43, self.height//6.7)

        exp_rect = exp.get_rect()
        exp_rect.topleft = (int(self.width//7.38), int(self.height//(-27)))

        rules_rect = rules.get_rect()
        rules_rect.topleft = (int(self.width//2.2), int(self.height//1.2))
        button_rules = pygame.Rect(int(self.width//2.2), int(self.height//1.2), int(self.width//12), int(self.height//7.4))

        font1 = pygame.font.Font('fonts/ARPU.otf', int(self.width//12.8))
        font2 = pygame.font.Font('fonts/ARPU.otf', int(self.width//30.72))
        font3 = pygame.font.Font('fonts/ARPU.otf', int(self.width//20))

        title = font1.render("Jeu de Nim", True, "white")
        self.screen.blit(title, (int(self.width//2.8), int(self.height//10.8)))

        pygame.draw.rect(self.screen, "white", (int(self.width//3), int(self.height//12.7), int(self.width//3), int(self.height//5.76)), 7, border_radius=15)

        pygame.draw.ellipse(self.screen, "#2582D7", (int(self.width//2.4), int(self.height//3.3), int(self.width//6.14), int(self.height//5.76)))
        button1 = pygame.Rect(int(self.width//2.4), int(self.height//3.3), int(self.width//6.14), int(self.height//5.76))
        pygame.draw.ellipse(self.screen, "#2582D7", (int(self.width//2.4), int(self.height//1.9), int(self.width//6.14), int(self.height//5.76)))
        button2 = pygame.Rect(int(self.width//2.4), int(self.height//1.9), int(self.width//6.14), int(self.height//5.76))

        pygame.draw.rect(self.screen, "#6699cc", (int(self.width//76.8), int(self.height//43.2), int(self.width//6.5), int(self.height//7.3)), border_radius=25)
        button_quit = pygame.Rect(int(self.width//76.8), int(self.height//43.2), int(self.width//6.5), int(self.height//7.3), border_radius=25)

        one_player_button_text = font2.render("Un Joueur", True, "white")
        two_players_button_text = font2.render("Deux Joueurs", True, "white")
        rules_button_text = font3.render("Regles", True, "white")
        quit_button_text = font3.render("Quitter", True, "white")

        self.screen.blit(one_player_button_text, (int(self.width//2.27), int(self.height//2.8)))
        self.screen.blit(two_players_button_text, (int(self.width//2.34), int(self.height//1.72)))
        self.screen.blit(rules_button_text, (int(self.width//2.28), int(self.height//1.35)))
        self.screen.blit(quit_button_text, (int(self.width//40), int(self.height//22)))

        one_player, two_players, rules_page = False, False, False
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.collidepoint(event.pos):
                        one_player = True
                    elif button2.collidepoint(event.pos):
                        two_players = True
                    elif button_rules.collidepoint(event.pos):
                        rules_page = True
                    elif button_quit.collidepoint(event.pos):
                        run = False

            if one_player:
                self.screen.fill("#175690")

                pygame.draw.rect(self.screen, "white", (int(self.width//3), int(self.height//12.7), int(self.width//3), int(self.height//5.76)), 7, border_radius=15)
                self.screen.blit(title, (int(self.width//2.8), int(self.height//10.8)))
                middle = pygame.Rect(int(self.width//2), int(self.height//2), 1, 1)

                character_rect1 = character_rect1.move(10, 0)
                self.screen.blit(character1, character_rect1)
                pygame.display.update()
                if character_rect1.colliderect(middle):
                    self.screen.fill("#175690")
                    self.screen.blit(exp, exp_rect)
                    pygame.display.flip()
                    time.sleep(1)
                    LoginPage(self.screen).login_one_user()
                    run = False

            elif two_players:
                self.screen.fill("#175690")
                    
                pygame.draw.rect(self.screen, "white", (int(self.width//3), int(self.height//12.7), int(self.width//3), int(self.height//5.76)), 7, border_radius=15)
                self.screen.blit(title, (int(self.width//2.8), int(self.height//10.8)))

                character_rect1 = character_rect1.move(10, 0)
                character_rect2 = character_rect2.move(-10, 0)
                self.screen.blit(character1, character_rect1)
                self.screen.blit(character2, character_rect2)
                pygame.display.update()
                if character_rect1.colliderect(character_rect2):
                    self.screen.fill("#175690")
                    self.screen.blit(exp, exp_rect)
                    pygame.display.flip()
                    time.sleep(1)
                    LoginPage(self.screen).login_two_user()
                    run = False

            elif rules_page:
                self.screen.fill("#175690")
                pygame.display.update()

            else:
                self.screen.blit(character1, character_rect1)
                self.screen.blit(character2, character_rect2)
                self.screen.blit(rules, rules_rect)
                pygame.display.update()

            self.clock.tick(60)

        pygame.quit()
