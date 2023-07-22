import pygame
from pygame.locals import *
import os

class buttens:
    def __init__(self,image,x,y,screen):
        self.image = image
        self.x = x
        self.y = y
        self.screen = screen
        rect = image.get_rect()
        self.rect = rect
        self.rect.left = self.x
        self.rect.top = self.y 
        self.butpre = False
        self.time = 100

    def ifpressed(self,event,mousex,mousey):
        # if self.butpre == True:
        #     self.butpre = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(mousex,mousey):
                return True
                # if self.butpre == False:
                #     self.butpre = True
        return False
                    


    def update(self):
        self.screen.blit(self.image,(self.x,self.y))
        # if self.butpre == True:
        #     self.screen.blit(self.imageon,(self.x,self.y))
        #     self.rect = self.imageon.get_rect()
        #     return True
            
        # else:
        #     self.screen.blit(self.imageoff,(self.x,self.y))
        #     self.rect = self.imageon.get_rect()
        #     return False

