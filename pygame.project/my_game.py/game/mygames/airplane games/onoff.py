import pygame
from pygame.locals import *
import os

class onoffclass:
    def __init__(self,screen,image_path):
        self.screen = screen
        self.image_path = image_path
        self.imageifon = 1
        self.imageon = pygame.image.load(os.path.join(image_path,"grey_box.png"))
        self.imageoff = pygame.image.load(os.path.join(image_path,"red_boxCheckmark.png"))
        self.rect = self.imageon.get_rect()

    
    def init(self,start_x,start_y):
        self.start_x = start_x
        self.start_y = start_y

    
    def ifpressed(self,event,mouse_x,mouse_y):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(mouse_x,mouse_y):
                if self.imageifon == 1:
                    self.imageifon = 0
                elif self.imageifon == 0:
                    self.imageifon == 1

                return True
        
        return False


    def update(self):
        if self.imageifon == 0:
            self.screen.blit(self.imageoff,(self.start_x,self.start_y))
        else:
            self.screen.blit(self.imageon,(self.start_x,self.start_y))

