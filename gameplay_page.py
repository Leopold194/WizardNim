import random

import pygame
from pygame.locals import *

import time

from game import Game
from result_page import ResultPage

class GameplayPage:
    
    def __init__(self, screen):

        self.height = pygame.display.Info().current_h
        self.width = pygame.display.Info().current_w

        self.clock = pygame.time.Clock()

        self.screen = screen

        wim1, him1, self.wim2, him2 = int(self.width//30.72), int(self.height//3.2), int(self.width//14.63), int(self.height//2.7)
        self.allumette01 = pygame.transform.scale(pygame.image.load("images/allumette.png").convert_alpha(), (wim1, him1))
        self.allumette02 = pygame.transform.scale(pygame.image.load("images/allumette2.png").convert_alpha(), (self.wim2, him2))

        self.ecart = (self.width-12*self.wim2)/13

        self.allumettes = [(self.allumette01.get_rect(), 0) for _ in range(12)]
        self.allumettes_button = [pygame.Rect(int((i+1)*self.ecart+i*self.wim2)+15, int(self.height//2.1), int(self.width//76.8), int(self.height//4.32)) for i in range(12)]

        for i in range(12):
            self.allumettes[i][0].topleft = (int((i+1)*self.ecart+i*self.wim2), self.height//2.54)        

        self.font1 = pygame.font.Font('fonts/ARPU.otf', int(self.width//8))
        self.font2 = pygame.font.Font('fonts/ARPU.otf', int(self.width//25))

    def one_player(self, name):

        computer_turn = self.font1.render("A Kurtain de jouer !", True, "white")
        player_turn = self.font1.render("A toi de jouer !", True, "white")
        continue_button_text = self.font2.render("Continuer", True, "white")

        game = Game()
        
        run = True
        nb, turn, time_to_wait = 0, 0, 0
        while game.remaining() >= 1 and run == True:
            
            if run:

                if turn == 0:
                    time_to_wait = 0
                    
                    self.screen.fill("#175690")

                    self.screen.blit(player_turn, (int(self.width//6), int(self.height//10.5)))
                    
                    pygame.draw.rect(self.screen, "#6699cc", (int(self.width//2.37), int(self.height//1.25), int(self.width//6.5), int(self.height//7.3)), border_radius=25)
                    continue_button = pygame.Rect(int(self.width//2.37), int(self.height//1.25), int(self.width//6.5), int(self.height//7.3), border_radius=25)
                    
                    self.screen.blit(continue_button_text, (int(self.width//2.31), int(self.height//1.2)))

            if run:

                if turn == 1:
                    self.screen.fill("#175690")
                    self.screen.blit(computer_turn, (int(self.width//14), int(self.height//10.5)))
                    result = game.computer_turn()
                    pygame.display.flip()
                    if result == 0:
                        ResultPage(self.screen).player_win(name)
                        run = False
                    else:
                        allumettes_lit = []
                        for i in self.allumettes:
                            if i[1] == 0:
                                allumettes_lit.append(self.allumettes.index(i))

                        for i in range(result):
                            x = random.choice(allumettes_lit)
                            del allumettes_lit[allumettes_lit.index(x)]
                            self.allumettes[x] = (self.allumette02.get_rect(), 1)
                            self.allumettes[x][0].topleft = (int((x+1)*self.ecart+x*self.wim2), self.height//3)
                            self.allumettes_button[x] = None

                    time_to_wait = 1
                    turn = 0

            if run:

                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        if turn == 0:
                            
                            for i in range(len(self.allumettes_button)):

                                if self.allumettes_button[i] != None: 
                                    if self.allumettes_button[i].collidepoint(event.pos) and nb < 3:
                                        self.allumettes[i] = (self.allumette02.get_rect(), 1)
                                        self.allumettes[i][0].topleft = (int((i+1)*self.ecart+i*self.wim2), self.height//3)
                                        self.allumettes_button[i] = None
                                        nb += 1
                                        break
                                    
                            if continue_button.collidepoint(event.pos) and nb > 0:
                                result = game.player_turn(nb)
                                if result == 0:
                                    ResultPage(self.screen).computer_win()
                                    run = False
                                nb = 0
                                turn = 1

            if run:
                
                for i in self.allumettes:
                    if i[1] == 0:
                        self.screen.blit(self.allumette01, i[0])
                    else:
                        self.screen.blit(self.allumette02, i[0])

                pygame.display.update()
                time.sleep(time_to_wait)
                
            self.clock.tick(60)
            

        pygame.quit()

    def two_players(self, name1, name2):

        player1_turn = self.font1.render(f"A {name1} de jouer !", True, "white")
        player2_turn = self.font1.render(f"A {name2} de jouer !", True, "white")

        player1_turn_rect = player1_turn.get_rect()
        player2_turn_rect = player2_turn.get_rect()

        player1_turn_rect.center = (int(self.width//2), int(self.height//5))
        player2_turn_rect.center = (int(self.width//2), int(self.height//5))

        continue_button_text = self.font2.render("Continuer", True, "white")

        game = Game()
        
        run = True
        nb, turn = 0, 0
        while game.remaining() >= 1 and run == True:
            
            if run:
                 
                self.screen.fill("#175690")

                if turn == 0:
                    self.screen.blit(player1_turn, player1_turn_rect)
                else:
                    self.screen.blit(player2_turn, player2_turn_rect)
                
                pygame.draw.rect(self.screen, "#6699cc", (int(self.width//2.37), int(self.height//1.25), int(self.width//6.5), int(self.height//7.3)), border_radius=25)
                continue_button = pygame.Rect(int(self.width//2.37), int(self.height//1.25), int(self.width//6.5), int(self.height//7.3), border_radius=25)
                
                self.screen.blit(continue_button_text, (int(self.width//2.31), int(self.height//1.2)))

            if run:

                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        
                            
                        for i in range(len(self.allumettes_button)):

                            if self.allumettes_button[i] != None: 
                                if self.allumettes_button[i].collidepoint(event.pos) and nb < 3:
                                    self.allumettes[i] = (self.allumette02.get_rect(), 1)
                                    self.allumettes[i][0].topleft = (int((i+1)*self.ecart+i*self.wim2), self.height//3)
                                    self.allumettes_button[i] = None
                                    nb += 1
                                    break
                                
                        if continue_button.collidepoint(event.pos) and nb > 0:
                            result = game.player_turn(nb)
                            if result == 0:
                                if turn == 0:
                                    ResultPage(self.screen).player_win(name2)
                                else:
                                    ResultPage(self.screen).player_win(name1)
                                run = False
                            nb = 0
                            if turn == 0:
                                turn = 1
                            else:
                                turn = 0

            if run:
                
                for i in self.allumettes:
                    if i[1] == 0:
                        self.screen.blit(self.allumette01, i[0])
                    else:
                        self.screen.blit(self.allumette02, i[0])

                pygame.display.update()
                
            self.clock.tick(60)
            

        pygame.quit()