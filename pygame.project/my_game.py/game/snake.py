import pygame
import time
import random

import os
screen = pygame.display.set_mode((700,700))
pygame.init()
image_path = "E:\siwoo\pygame.project\my_game.py\game/images"
# start_but = pygame.image.load(os.path.join(image_path,"startbut.png")).convert_alpha()
# invis = 0
# invis1 = 1
fors = 0
font = pygame.font.Font(None, 80)
snaketurn = []
class snakebod:
    def __init__(self,x,y,own):
        self.snakeb = pygame.Surface((50,50))
        self.snakeb.fill((255,255,255))
        self.snakenum = 0

        self.x = x
        self.y = y
        self.ownnum = own
        self.dir = "right"

    def go(self):
        if self.dir == "right":
            self.x += 50
        if self.dir == "left":
            self.x -= 50
        if self.dir == "up":
             self.y -= 50
        if self.dir == "down":
             self.y += 50
        
    
    def update(self):

            screen.blit(self.snakeb,(self.x,self.y))
class fruit:
    def __init__(self):
        self.point = 0
        self.x = random.randint(0,700)
        self.y = random.randint(110,700)
        self.cir = pygame.draw.circle(screen,(255,255,255),(self.x,self.y),25)
        self.hitbox = pygame.Surface((3,3))
        self.ptext = font.render(str(self.point) + "points.", True, (255, 255, 255))
        if self.x % 50 != 0:
            for i in range(10):
                self.x += 1
                if self.x % 50 == 0:
                    break
        if self.y % 50 != 0:
            for i in range(10):
                self.y += 1
                if self.y % 50 == 0:
                    break
        
    
    def getp(self,sr):
        hibr = self.hitbox.get_rect()
        hibr.left = self.x - 2.5
        hibr.top = self.y-2.5

        if hibr.colliderect(sr):
        
            self.point += 1
            return True
        return False
        
    def sum(self):
        self.x = random.randint(0,700)
        self.y = random.randint(0,700)
        if self.x % 5 != 0:
            for i in range(999999999999999999999):
                self.x += 1
                if self.x % 5 == 0:
                    
                    break
        if self.y % 5 != 0:
            for i in range(10):
                self.y += 1
                if self.y % 5 == 0:
                
                    
                    break



    
    def update(self):
        screen.blit(self.hitbox,(self.x - 2.5,self.y-2.5))
        self.cir = pygame.draw.circle(screen,(255,255,255),(self.x,self.y),25)
        self.ptext = font.render(str(self.point) + "points.", True, (255, 255, 255))
        screen.blit(self.ptext,(200,50))
        

for i in range(140):
    
    pygame.draw.line(screen,(255,255,255) ,(0,0 + i * 5),(700,0 + i * 5),width=1)
pblock = pygame.Surface((700,10))
fruit1 = fruit()
snakes = []
for s in range(1,3):
    snakes.append(snakebod(350 - s * 50,350,s))

eye1 = pygame.Surface((10,10))
eye2 = pygame.Surface((10,10))

game = True
fruit1.sum()
while game:
    screen.fill((0,0,0))
    time.sleep(0.2)


    for x in snaketurn:
        x[0] += 1
        for i in snakes:
            
            i.update()
            
            if i.ownnum == x[0]:
                i.dir = x[1]
    sr = snakes[0].snakeb.get_rect()
    sr.left = snakes[0].x
    sr.top= snakes[0].y   
            
    if fruit1.getp(sr):
        fruit1.sum()


    for i in snakes:
        i.go()
        i.update()

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            for i in [[pygame.K_UP,"down","up"],[pygame.K_DOWN,"up","down"],[pygame.K_LEFT,"right","left"],[pygame.K_RIGHT,"left","right"]]:
                if event.key == i[0]:
                
                    if snakes[0].dir != i[1]:
                        snakes[0].dir = i[2]
                        snaketurn.append([0,i[2]])

    screen.blit(eye1,(snakes[0].x + 3,snakes[0].y + 3.5))
    screen.blit(eye2,(snakes[0].x + 3,snakes[0].y + 1.5))
    pblock.fill((255,255,255))
    screen.blit(pblock,(0,100))
    for i in range(140):
        
        pygame.draw.line(screen,(255,255,255) ,(0,0 + i * 50),(700,0 + i * 50),width=10)
    
    fruit1.update()

    pygame.display.update()

