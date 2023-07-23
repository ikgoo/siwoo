import pygame
from settings import *

class UI:
    def __init__(self):
        self.display_suf = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        
        # bar setup
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)
        
        self.weapon_grhpics = []
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_grhpics.append(weapon)
            self.magic_grhpics = []
            for magic1 in magic_data.values():
                magic = pygame.image.load(magic1['graphics']).convert_alpha()
                self.magic_grhpics.append(magic)
    def show_bar(self,current,max_amount,bg_rect,color):
        pygame.draw.rect(self.display_suf,UI_BG_COLOR,bg_rect)
        
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        
        
        pygame.draw.rect(self.display_suf,color,current_rect)
        pygame.draw.rect(self.display_suf,UI_BORDER_COLOR,bg_rect,3)
        
    def selection_box(self,left,top, has_swiched):
        bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		
        pygame.draw.rect(self.display_suf,UI_BG_COLOR,bg_rect)
        if not has_swiched:
            pygame.draw.rect(self.display_suf,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
        else:
        
            pygame.draw.rect(self.display_suf,UI_BORDER_COLOR,bg_rect,3)
        return bg_rect
    
    def weapon_overlay(self,weapon_index,has_swiched):
        bg_rect = self.selection_box(10,630 ,has_swiched) #weapon
        weapon_surf = self.weapon_grhpics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
        
        self.display_suf.blit(weapon_surf,weapon_rect)
    

    def magic_overlay(self,magic_index,has_switched):
        bg_rect = self.selection_box(80,635 ,has_switched) #weapon
        magic_surf = self.magic_grhpics[magic_index]
        magic_rect = magic_surf.get_rect(center = bg_rect.center)
        
        self.display_suf.blit(magic_surf,magic_rect)
    




    def display(self,player):
        self.show_bar(player.health,player.states['health'],self.health_bar_rect,HEALTH_COLOR)
        self.show_bar(player.energy,player.states['energy'],self.energy_bar_rect,ENERGY_COLOR)
        
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index,player.can_switch)
        self.magic_overlay(player.magic_index,player.can_swicth_magic)
        
    def show_exp(self,exp):
        text_Surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
        x = self.display_suf.get_size()[0] - 20
        y = self.display_suf.get_size()[1] - 20
        text_rect = text_Surf.get_rect(bottomright = (x,y))
        pygame.draw.rect(self.display_suf,UI_BG_COLOR,text_rect.inflate(20,20))
        self.display_suf.blit(text_Surf,text_rect)
        pygame.draw.rect(self.display_suf,UI_BORDER_COLOR,text_rect.inflate(20,20),3)