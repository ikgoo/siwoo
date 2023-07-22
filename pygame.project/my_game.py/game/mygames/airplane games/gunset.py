import pygame
import os
import gamemenuclass
import butten
from pytmx import load_pygame
class gunsett:
    def __init__(self,screen,image_path):
        self.screen = screen
        self.blocks = []
        self.surfacex = 0
        self.surfacey = 0
        self.surface2x = 0
        self.surface2y = -900
        self.ship_path = "E:/siwoo/pygame.project/my_game.py/game/images/ships"
        self.image_path = image_path
        arrow_ima = pygame.image.load(os.path.join(self.image_path,"black arrow.png"))
        arrow_ima1 = pygame.image.load(os.path.join(self.image_path,"black arrow.png"))
        arrow_ima1 = pygame.transform.flip(arrow_ima1,True,False)
        self.arrow1 = butten.buttens(arrow_ima,300,400,self.screen)
        self.arrow2 = butten.buttens(arrow_ima1,150,400,self.screen)
        on = pygame.image.load(os.path.join(self.image_path,"red_button06_back.png"))
        self.outbut = butten.buttens(on,300,800,self.screen)
        
        self.ship_num = 0
        ship1 = pygame.image.load(os.path.join(self.ship_path,"ship_0000.png"))
        ship2 = pygame.image.load(os.path.join(self.ship_path,"ship_0001.png"))
        ship3 = pygame.image.load(os.path.join(self.ship_path,"ship_0002.png"))
        ship4 = pygame.image.load(os.path.join(self.ship_path,"ship_0003.png"))
        ship5 = pygame.image.load(os.path.join(self.ship_path,"ship_0004.png"))
        self.ships = [ship1,ship2,ship3,ship4,ship5]


        self.surface = pygame.Surface((500, 900))
        self.surface2 = pygame.Surface((500,900))
        tmx_data = load_pygame("E:/siwoo/pygame.project/my_game.py/game/images/siwoomap.tmx")
        obj_l = tmx_data.get_layer_by_name("Tile Layer 1")
        for obj in tmx_data.visible_layers:
            if hasattr(obj,"data"):
                for x,y,surf in obj.tiles():

                    pos = (x*16,y*16)
                    self.surface.blit(surf, (pos))
                    self.surface2.blit(surf, (pos))

    def going(self):
        
        

        
        self.surfacey += round(0.5,1)
        if self.surfacey == 900:
            self.surfacey = -900
        self.surface2y += round(0.5,1)
        if self.surface2y == 900:
            self.surface2y = -900
        
        self.screen.fill((255,255,255))
        self.screen.blit(self.surface,(self.surfacex,self.surfacey))
        self.screen.blit(self.surface2,(self.surface2x,self.surface2y))

    def ship_change(self,event,mousex,mousey):
        if self.arrow2.ifpressed(event,mousex,mousey):
            if self.ship_num != 0:
                self.ship_num -= 1
        if self.arrow1.ifpressed(event,mousex,mousey):
            if self.ship_num != len(self.ships)-1:
                self.ship_num += 1
        if self.outbut.ifpressed(event,mousex,mousey) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return True
    def update(self):
        self.arrow1.update()
        self.arrow2.update()
        self.screen.blit(self.ships[self.ship_num],(230,420))
        self.outbut.update()
        pygame.display.update()

           