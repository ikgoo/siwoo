
import pygame
import os
import butten
import gunset


class gamemenu:
    def __init__(self,screen,image_path):
        self.screen = screen
        self.image_path = image_path
        image = pygame.image.load(os.path.join(self.image_path,"red_button06_change.png"))
        on = pygame.image.load(os.path.join(self.image_path,"red_button06_back.png"))
        self.outbut = butten.buttens(on,300,800,self.screen)
        
        self.gunbut = butten.buttens(image,400,700,self.screen)
        self.gunset = gunset.gunsett(self.screen,image_path)
    
    def ifpressed(self,event):
        
        mousex,mousey = pygame.mouse.get_pos()
        pre = self.gunbut.ifpressed(event,mousex,mousey)
        if self.outbut.ifpressed(event,mousex,mousey) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return True
        if pre == True:
            while pre:
                mousex,mousey = pygame.mouse.get_pos()
                self.gunset.going()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pre = False


                    
                    if self.gunset.ship_change(event,mousex,mousey):
                        pre = False
                self.gunset.update()
                pygame.display.update()
                

                
        
    
    
    def update(self):
        self.screen.fill((0,0,255))
        self.gunbut.update()
        self.outbut.update()
        pygame.display.update()
 