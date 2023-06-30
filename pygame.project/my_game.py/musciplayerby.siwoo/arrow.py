import pygame
class arrow:
    def __init__(self,arrow_number,screen,musics,game_font,arrow_y,first,arrow_number_see):
        self.arrow_number = arrow_number
        self.screen = screen
        self.musics = musics
        self.game_font = game_font
        self.arrow_number = arrow_number
        self.arrow_y = arrow_y
        self.first = first
        self.arrow_number_see = arrow_number_see

    def key_pushed(self,event):
        if event.key == pygame.K_DOWN:
            if len(self.musics) > self.arrow_number:
                self.arrow_number_see = self.arrow_number
                self.arrow_number += 1
                
                self.first = 0
        
            #else 

        if event.key == pygame.K_UP:
            if 1 < self.arrow_number:
                self.arrow_number_see = self.arrow_number
                self.arrow_number -= 1
                    
                self.first = 0
                
        return self.arrow_number                

    def update(self,first):
            if self.arrow_number - self.arrow_number_see == 1:
                
                arrow = self.game_font.render(">",True,(255,255,255))
                arrow_font = arrow.get_rect()
                if self.first == 0:
                    self.arrow_y += 100
                arrow_font.center = (50,self.arrow_y)
                self.screen.blit(arrow,arrow_font)
                self.first = 1
                
            if self.arrow_number - self.arrow_number_see == -1:
                arrow = self.game_font.render(">",True,(255,255,255))
                arrow_font = arrow.get_rect()
                if self.first == 0:
                    self.arrow_y -= 100
                self.first = 1
                arrow_font.center = (50,self.arrow_y)
            self.screen.blit(arrow,arrow_font)
