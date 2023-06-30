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
snaketurn = []
class snakebod:
    def __init__(self,x,y,own):
        self.snake = pygame.Surface((10,10))
        self.snake.fill((255,255,255))
        self.snakenum = 0

        self.x = x
        self.y = y
        self.ownnum = own
        self.dir = "right"

    def go(self):
        if self.dir == "right":
            self.x += 10
        if self.dir == "left":
            self.x -= 10
        if self.dir == "up":
             self.y -= 10
        if self.dir == "down":
             self.y += 10
        
    
    def update(self):

            screen.blit(self.snake,(self.x,self.y))
class fruit:
    def __init__(self):
        self.point = 0
        self.x = 0
        self.y = 0
    
    def getp(self):
        
    def sum(self):
        self.x = random.randint(0,700)
        self.y = random.randint(0,700)
        pygame.draw.circle(self.x,self.y)
        


snakes = []
for s in range(0,2):
    snakes.append(snakebod(350 + s * 10,350,s))

eye1 = pygame.Surface((2,2))
eye2 = pygame.Surface((2,2))

game = True
while game:
    screen.fill((0,0,0))
    time.sleep(0.1)


    for x in snaketurn:
        x[0] += 1
        for i in snakes:
            
            i.update()
            
            if i.ownnum == x[0]:
                i.dir = x[1]
            
            
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
    pygame.display.update()

    