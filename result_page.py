import pygame
from pygame.locals import *

import time
from random import randint

import menu_nim as MN

class Item:

    def __init__(self, pic, pos, type):

        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        size = (int(self.width//13.36), int(self.height//3.84)) if type == "balloon" else (int(self.width//8.3), int(self.height//5.24)) if type == "explosion" else None
        
        self.pic = pygame.transform.scale(pygame.image.load(pic).convert_alpha(), size)
        self.rect = self.pic.get_rect()
        self.rect.topleft = pos
        self.vitesse = randint(2, 6)

    def move(self):
        self.rect = self.rect.move(0, -self.vitesse)

    def exp(self):
        self.rect = self.rect.move(0, 0)

    def display(self, screen):
        screen.blit(self.pic, self.rect)


class ResultPage:

    def __init__(self, screen):

        self.screen = screen
        
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

        self.font1 = pygame.font.Font('fonts/ARPU.otf', int(self.width//10))
        self.font2 = pygame.font.Font('fonts/ARPU.otf', int(self.width//20))

        self.button_quit = pygame.transform.scale(pygame.image.load('images/cross.png'), (int(self.width//22.26), int(self.height//12.52)))
        self.button_quit_rect = self.button_quit.get_rect()
        self.button_quit_rect.topleft = (int(self.width - self.width//15.36), int(self.width//43.2))

    def computer_win(self):

        pygame.mixer.music.load("musics/music_lose.wav")
        pygame.mixer.music.play(-1)

        text_list = [("K", int(self.width//6.144)), ("u", int(self.width//4.8)), ("r", int(self.width//3.94)), ("t", int(self.width//3.34)), ("a", int(self.width//2.98)), ("i", int(self.width//2.6)), ("n", int(self.width//2.44)), ("a", int(self.width//2.08)), ("g", int(self.width//1.79)), ("a", int(self.width//1.67)), ("g", int(self.width//1.54)), ("n", int(self.width//1.44)), ("e", int(self.width//1.35)), ("!", int(self.width//1.25))]
        text1 = self.font2.render("Retente une prochaine fois", True, "white")

        explosions = []

        x, y = 0, []
        run = True
        while run :
            
            x += 1

            if randint(1,500) <= 100 and x > len(text_list):
                explosions.append(Item('images/explosion.png',(randint(-int(self.width//8.3), int(self.width+(self.width//8.3))), randint(-int(self.height//5.24), int(self.height+self.height//5.24))), "explosion"))
                
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_quit_rect.collidepoint(event.pos):
                        MN.Menu(self.screen).menu()
                        run = False
            
            self.screen.fill("#175690")
            if x > len(text_list) * 10:
                self.screen.blit(text1, (int(self.width//3.6), int(self.height//1.57)))

            for i in range(x):
                try:
                    letter_info = text_list[i]
                    self.screen.blit(self.font1.render(letter_info[0], True, "white"), (letter_info[1], self.height//3))
                    if letter_info not in y:
                        time.sleep(0.2)
                    y.append(letter_info)
                except:
                    pass

            for explosion in explosions:
                explosion.display(self.screen)

            self.screen.blit(self.button_quit, self.button_quit_rect)

            pygame.display.update()

        pygame.quit()

    def player_win(self, winner):

        pygame.mixer.music.load("musics/music_win.wav")
        pygame.mixer.music.play(-1)

        text_list = [("a", int(self.width//3.13)), ("g", int(self.width//2.52)), ("a", int(self.width//2.29)), ("g", int(self.width//2.08)), ("n", int(self.width//1.90)), ("e", int(self.width//1.74)), ("!", int(self.width//1.57))]
        text1 = self.font2.render("Bravo a toi ! Tu es le meilleur !", True, "white")

        balloons = []

        x, y = 0, []
        run = True
        while run :
            
            x += 1

            if len(balloons)<30 and randint(1,500)<=30 and x > len(text_list):
                balloons.append(Item(f'images/balloon{randint(1, 6)}.png',(randint(0, self.width), self.height+int(self.height//5.24)), "balloon"))
            
            self.screen.fill("#175690")
            self.screen.blit(self.font1.render(winner, True, "white"), self.font1.render(winner, True, "white").get_rect(center=(self.width//2, self.height//3.5)))
            self.screen.blit(self.button_quit, self.button_quit_rect)
            if x > len(text_list) * 10:
                self.screen.blit(text1, text1.get_rect(center = (self.width//2, int(self.height//1.44))))

            for i in range(x):
                try:
                    letter_info = text_list[i]
                    self.screen.blit(self.font1.render(letter_info[0], True, "white"), (letter_info[1], self.height//2.8))
                    if letter_info not in y:
                        time.sleep(0.2)
                    y.append(letter_info)
                except:
                    pass

            for balloon in balloons:
                balloon.move()
                if balloon.rect.top <= -int(self.height//3.84):
                    balloons.remove(balloon)
                else :
                    balloon.display(self.screen)

            for event in pygame.event.get():
                
                if event.type == QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_quit_rect.collidepoint(event.pos):
                        MN.Menu(self.screen).menu()
                        run = False
            
            if run:
                pygame.display.update()

        pygame.quit()