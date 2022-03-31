import pygame
from pygame.locals import *

from gameplay_page import GameplayPage

class LoginPage:

    def __init__(self, screen):

        self.screen = screen
        self.screen.fill("#175690")
        
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.clock = pygame.time.Clock()

        self.font1 = pygame.font.Font('fonts/ARPU.otf', int(self.width//40))
        self.font2 = pygame.font.Font('fonts/ARPU.otf', int(self.width//20))
        self.font3 = pygame.font.Font('fonts/ARPU.otf', int(self.width//15))

        self.button_quit = pygame.transform.scale(pygame.image.load('images/cross.png'), (int(self.width//22.26), int(self.height//12.52)))
        self.button_quit_rect = self.button_quit.get_rect()
        self.button_quit_rect.topleft = (int(self.width - self.width//15.36), int(self.width//43.2))

        pygame.draw.rect(self.screen, "#3795CC", (int(self.width//2.48), int(self.height//1.44), int(self.width//5.12), int(self.height//8.64)), border_radius=25)
        self.button_continue = pygame.Rect(int(self.width//2.48), int(self.height//1.44), int(self.width//5.12), int(self.height//8.64), border_radius=25)

        pygame.mixer.music.load("musics/music_menu.wav")
        pygame.mixer.music.play(-1)

    def login_one_user(self):

        text1 = self.font2.render("Nom de votre joueur :", True, "white")
        text1_rect = text1.get_rect()
        text1_rect.center = (self.width//2, self.height//3)

        text2 = self.font1.render("Entre 3 et 14 Caracteres !", True, "white")
        text2_rect = text2.get_rect()
        text2_rect.center = (self.width//2, self.height//1.8)
        
        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)

        pygame.draw.rect(self.screen, "#3795CC", (int(self.width//2.48), int(self.height//1.44), int(self.width//5.12), int(self.height//8.64)), border_radius=25)
        button_continue = pygame.Rect(int(self.width//2.48), int(self.height//1.44), int(self.width//5.12), int(self.height//8.64), border_radius=25)

        text3 = self.font3.render("Valider", True, "#175690")
        text3_rect = text3.get_rect()
        text3_rect.center = (self.width//2, self.height//1.33)
        self.screen.blit(text3, text3_rect)

        input1 = pygame.Rect(int(self.width//3.41), int(self.height//2.43), int(self.width//2.4), int(self.height//12.34))

        active1, user_name = False, ''
        run = True
        while run:
                
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.button_quit_rect.collidepoint(event.pos):
                        run = False

                    if input1.collidepoint(event.pos):
                        active1 = True

                    if button_continue.collidepoint(event.pos) and len(user_name) >= 3:
                        GameplayPage(self.screen).one_player(user_name)
                        run = False

                if event.type == pygame.KEYDOWN:
                    
                    if active1:
                        if event.key == pygame.K_BACKSPACE:
                            user_name = user_name[:-1]
                        else:
                            if len(user_name) <= 14 and (event.unicode.isalpha() or event.unicode.isdigit()):
                                user_name += event.unicode
        
            if active1:
                color1 = "#cbbcdb"
            else:
                color1 = "white"

            pygame.draw.rect(self.screen, color1, input1)

            text_surface = self.font2.render(user_name, True, "purple")
            self.screen.blit(text_surface, (int(self.width//3.38), int(self.height//2.47)))

            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()

    def login_two_user(self):

        text_player1 = self.font2.render("Nom du premier joueur :", True, "white")
        text_player1_rect = text_player1.get_rect()
        text_player1_rect.center = (self.width//2, self.height//6.5)

        text_player2 = self.font2.render("Nom du deuxieme joueur :", True, "white")
        text_player2_rect = text_player2.get_rect()
        text_player2_rect.center = (self.width//2, self.height//2.7)

        text1 = self.font1.render("Entre 3 et 14 Caracteres !", True, "white")
        text1_rect = text1.get_rect()
        text1_rect.center = (self.width//2, self.height//1.7)
        
        self.screen.blit(text_player1, text_player1_rect)
        self.screen.blit(text_player2, text_player2_rect)
        self.screen.blit(text1, text1_rect)

        pygame.draw.rect(self.screen, "#3795CC", (int(self.width//2.48), int(self.height//1.44), int(self.width//5.12), int(self.height//8.64)), border_radius=25)
        button_continue = pygame.Rect(int(self.width//2.48), int(self.height//1.44), int(self.width//5.12), int(self.height//8.64), border_radius=25)

        text3 = self.font3.render("Valider", True, "#175690")
        text3_rect = text3.get_rect()
        text3_rect.center = (self.width//2, self.height//1.33)
        self.screen.blit(text3, text3_rect)

        input1 = pygame.Rect(int(self.width//3.41), int(self.height//4.55), int(self.width//2.4), int(self.height//12.34))
        input2 = pygame.Rect(int(self.width//3.41), int(self.height//2.27), int(self.width//2.4), int(self.height//12.34))

        active1, active2, user1_name, user2_name = False, False, '', ''
        run = True
        while run:
                
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.button_quit_rect.collidepoint(event.pos):
                        run = False

                    if input1.collidepoint(event.pos):
                        active1 = True
                        active2 = False
                    elif input2.collidepoint(event.pos):
                        active2 = True
                        active1 = False

                    if button_continue.collidepoint(event.pos) and len(user1_name) >= 3 and len(user2_name) >= 3:
                        GameplayPage(self.screen).two_players(user1_name, user2_name)
                        run = False

                if event.type == pygame.KEYDOWN:
                    
                    if active1:
                        if event.key == pygame.K_BACKSPACE:
                            user1_name = user1_name[:-1]
                        else:
                            if len(user1_name) <= 14 and (event.unicode.isalpha() or event.unicode.isdigit()):
                                user1_name += event.unicode
                    elif active2:
                        if event.key == pygame.K_BACKSPACE:
                            user2_name = user2_name[:-1]
                        else:
                            if len(user2_name) <= 14 and (event.unicode.isalpha() or event.unicode.isdigit()):
                                user2_name += event.unicode
        
            if active1:
                color1 = "#cbbcdb"
                color2 = "white"
            elif active2:
                color1 = "white"
                color2 = "#cbbcdb"
            else:
                color1, color2 = "white", "white"

            pygame.draw.rect(self.screen, color1, input1)
            pygame.draw.rect(self.screen, color2, input2)

            text_user1 = self.font2.render(user1_name, True, "purple")
            self.screen.blit(text_user1, (int(self.width//3.36), int(self.height//4.67)))

            text_user2 = self.font2.render(user2_name, True, "purple")
            self.screen.blit(text_user2, (int(self.width//3.36), int(self.height//2.32)))

            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()



