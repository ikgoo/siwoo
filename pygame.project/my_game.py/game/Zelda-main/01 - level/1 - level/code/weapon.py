import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        dir = player.status.split('_')[0]
        full_path = f'..\\graphics\\weapons\\{player.weapon}\\{dir}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        if dir == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
        elif dir == 'left':
            
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
        elif dir == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
		
        elif dir == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))
        else:
            self.rect = self.image.get_rect(center = player.rect.center)
        