import pygame


class weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        dir = player.status.split('_')[0]
        
        self.image = pygame.Surface((40,40))
        if dir == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
        elif dir == 'left':
            
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
        
        else:
            self.rect = self.image.get_rect(center = player.rect.center)
        	
        
