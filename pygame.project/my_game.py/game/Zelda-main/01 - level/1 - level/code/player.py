import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_spr):
        super().__init__(groups)
        self.image = pygame.image.load('..\\graphics\\test\\player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.dir = pygame.math.Vector2()
        self.speed = 5
        self.obs_spr = obstacle_spr
  
    def input(self):
        keys = pygame.key.get_pressed()
  

        if keys[pygame.K_s]:
            self.dir.y = 1
   
        elif keys[pygame.K_w]:
            self.dir.y = -1
        else:
            self.dir.y = 0
   
        if keys[pygame.K_a]:
            self.dir.x = -1
   
        elif keys[pygame.K_d]:
            self.dir.x = 1
        else:
            self.dir.x = 0
        if keys[pygame.K_SPACE]:
            print('attack')
        if keys[pygame.K_LCTRL]:
            print('magic')
    def move(self,speed):
        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()
        self.hitbox.x += self.dir.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.dir.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center
        

    def collision(self,dir):
        if dir == "horizontal":
            for sprite in self.obs_spr:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.dir.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.dir.x < 0:
                        self.hitbox.left = sprite.hitbox.right

                        
        if dir == "vertical":
            for sprite in self.obs_spr:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.dir.y > 0: # moving right
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.dir.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
  
    def update(self):
        self.input()
        self.move(self.speed)
    
            
    
        
      
            
  