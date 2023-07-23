import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.dir = pygame.math.Vector2()

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
    