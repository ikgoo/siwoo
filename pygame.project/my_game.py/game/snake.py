import pygame
import time
import random
import numpy as np
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
ch = 0
snakehitbox = pygame.draw.rect(screen,(255,255,255),(350,350,25,25))
clock = pygame.time.Clock()
dt = clock.tick(50)
snx = 350
sny = 350
getped = 0
snakerect = []
class snakebod:
    def __init__(self,x,y,own):
        self.snakeb = pygame.Surface((25,25))
        self.snakeb.fill((255,255,255))
        self.snakenum = 0

        self.x = x
        self.y = y
        self.ownnum = own
        self.dir = "right"
        
        self.fall = -0.2
        
        self.eye1 = pygame.Surface((10,10))

    def go(self):
        if self.dir == "right":
            if snakes[0].x >= 700:
                pass
            else:
                self.x += 25
        if self.dir == "left":
            if snakes[0].x <= 0:
                pass
            else:
                self.x -= 25
        if self.dir == "up":
            if snakes[0].y <= 100:
                pass
            else:
                self.y -= 25
        if self.dir == "down":
            if snakes[0].y >= 700:
                pass
            else:
                self.y += 25

    
    def update(self):
        screen.blit(self.snakeb,(self.x,self.y))


class fruit:
    def __init__(self):
        self.point = 0
        self.x = random.randint(0,700)
        self.y = random.randint(110,700)
        self.cir = pygame.draw.circle(screen,(255,255,255),(self.x,self.y),7.5)
        self.hitbox = pygame.Surface((3,3))
        self.ptext = font.render(str(self.point) + "points.", True, (255, 255, 255))
        if self.x % 50 != 0:
            for i in range(10):
                self.x += 1
                if self.x % 50 == 0:
                    self.x += 7.5
                    break
        if self.y % 50 != 0:
            for i in range(10):
                self.y += 1
                if self.y % 50 == 0:
                    self.y += 7.5
                    break

        
    
    def getp(self):
        hibr = self.hitbox.get_rect()
        hibr.left = self.x - 2.5
        hibr.top = self.y-2.5

        if hibr.colliderect(snakehitbox):
            self.point += 1
            for c in snakes:
                c.ownnum = c.ownnum + 1
            if snakes[0].dir == "up":
                snakes.insert(0,snakebod(snx,sny,1))
            elif snakes[0].dir == "down":
                snakes.insert(0,snakebod(snx,sny,1))
            elif snakes[0].dir == "left":
                snakes.insert(0,snakebod(snx,sny,1))
            elif snakes[0].dir == "right":
                snakes.insert(0,snakebod(snx,sny,1))
            snakes[0].dir = snakes[1].dir
            return True
        return False
            
            
            
                
        
    def sum(self):
        self.x = random.randint(25,700)
        self.y = random.randint(110,700)
        if self.x % 5 != 0:
            while True:
                self.x += 1
                if self.x % 5 == 0:
                    
                    break
        if self.y % 5 != 0:
            while True:
                self.y += 1
                if self.y % 5 == 0:
                
                    
                    break



    
    def update(self):
        screen.blit(self.hitbox,(self.x - 2.5,self.y-2.5))
        self.cir = pygame.draw.circle(screen,(255,255,255),(self.x,self.y),7.5)
        self.ptext = font.render(str(self.point) + "points.", True, (255, 255, 255))
        screen.blit(self.ptext,(200,50))
def hitbox():
    global snakes
    global snx
    global sny
    global screen
    global snakehitbox
    if snakes[0].dir == "right":
        snakehitbox = pygame.draw.rect(screen,(0,0,0),(snakes[0].x + 25,snakes[0].y,25,25))
        snx=snakes[0].x + 25
    if snakes[0].dir == "left":
        snakehitbox = pygame.draw.rect(screen,(0,0,0),(snakes[0].x - 25,snakes[0].y,25,25))
        snx = snakes[0].x - 25
    if snakes[0].dir == "up":
            snakehitbox = pygame.draw.rect(screen,(0,0,0),(snakes[0].x,snakes[0].y - 25,25,25))
            sny = snakes[0].y - 25
    if snakes[0].dir == "down":
            snakehitbox = pygame.draw.rect(screen,(0,0,0),(snakes[0].x,snakes[0].y + 25,25,25))
            sny = snakes[0].y + 25
        

for i in range(140):
    pygame.draw.line(screen,(255,255,255) ,(0,0 + i * 5),(700,0 + i * 5),width=1)

pblock = pygame.Surface((700,10))
fruit1 = fruit()
snakes = []

for s in range(1,4):
    snakes.append(snakebod(350 - s * 25 + 1,350+1,s))


eye1 = pygame.Surface((10,10))
eye2 = pygame.Surface((10,10))
cene = 0
game = True
fruit1.sum()
menu = True
msnakes = []
# while menu:
#     screen.fill((255,255,255))
    
#     snake_game = font.render("SNAKE GAME",True,(0,0,0))
#     screen.blit(snake_game,(150,200))
#     for s in range(1,4):
#         msnakes.append(snakebod(350 - s * 25 + 1,350+1,s))

#     if cene == 4:
#         msnakes[0].dir = "up"
#     if cene == 7:
#         msnakes[0].dir = "left"
#     if cene == 
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game = False
#         if event.type == pygame.KEYDOWN:
#             for i in [[pygame.K_UP,"down","up"],[pygame.K_DOWN,"up","down"],[pygame.K_LEFT,"right","left"],[pygame.K_RIGHT,"left","right"]]:
#                 if event.key == i[0]:
                
#                     if snakes[0].dir != i[1]:
#                         if snaketurn != []:
#                             if snaketurn[0][0] == 0:
#                                 break
#                             else:
#                                 snakes[0].dir = i[2]
                            
#                                 snaketurn.append([0,i[2]])
#                         else:
#                             snakes[0].dir = i[2]
                        
#                             snaketurn.append([0,i[2]])
                        

#     screen.blit(eye1,(snakes[0].x + 10,snakes[0].y + 5))

        
    
def died():
    global game
    global sr
    global screen
    for z in snakes:
        
        if snakes[0] .x <= 0 or snakes[0].x >= 700 or snakes[0].y <= 100 or snakes[0].y >= 700 or (snakes[0].x == z.x and z != snakes[0] and snakes[0].y == z.y):
            time.sleep(1.5)

            timer = time.time()
            
            while True:
                
                pygame.draw.rect(screen,(100,200,0),(0,100,700,600))
                for i in range(28):
	        
                    pygame.draw.line(screen,(0,255,0) ,(0,100 + i * 25),(700,100 + i * 25),width=10)
                    pygame.draw.line(screen,(0,255,0) ,(0 + i * 25,100),(0 + i * 25,700),width=10)
                pblock.fill((255,255,255))
                screen.blit(pblock,(0,100))
                for c in snakes:
                    c.update()
                
                chk = False
                for x in snakes:
                    if x.y <= 700:
                        chk = True
                        break
                if chk == False:
                    break
                    
                end_t = time.time()
                
                for index, x in enumerate(snakes):
                    if index != 0:

                        if end_t - timer < (0.2 * index):
                            continue
                    
                    if x.x >= 701:
                        x.x = 675
                    if x.x <= 0:
                        x.x = 0
                    x.y += x.fall
                    x.fall += round(0.001,4)
                    x.update()
                    if index == 0:
                        screen.blit(eye1,(snakes[0].x + 10,snakes[0].y+5))

            game = False
            break
            # gameover = pygame.font.render("game over", True, (255,0,50))
    
    # pygame.display.update()

while game:
    time.sleep(0.1)
    hitbox()

    screen.fill((0,0,0))
    


    for x in snaketurn:
        x[0] += 1
        for i in snakes:
            
            i.update()
            
            if i.ownnum == x[0]:
                i.dir = x[1]
    sr = snakes[0].snakeb.get_rect()
    sr.left = snakes[0].x
    sr.top= snakes[0].y
    for u in snakes:
        snakerect.append(u.snakeb.get_rect())
        snakerect[-1].left = u.x
        snakerect[-1].top = u.y
            
    if fruit1.getp():
        getped =1
        fruit1.sum()
    pygame.draw.rect(screen,(100,200,0),(0,100,700,600))

    for i in range(28):
        pygame.draw.line(screen,(0,255,0) ,(0,100 + i * 25),(700,100 + i * 25),width=10)
        pygame.draw.line(screen,(0,255,0) ,(0 + i * 25,100),(0 + i * 25,700),width=10)

    for i in snakes:
        if getped == 0:
            i.go()
        i.update()
    
    if getped == 1:
        getped = 0
     
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            for i in [[pygame.K_UP,"down","up"],[pygame.K_DOWN,"up","down"],[pygame.K_LEFT,"right","left"],[pygame.K_RIGHT,"left","right"]]:
                if event.key == i[0]:
                
                    if snakes[0].dir != i[1]:
                        if snaketurn != []:
                            if snaketurn[0][0] == 0:
                                break
                            else:
                                snakes[0].dir = i[2]
                            
                                snaketurn.append([0,i[2]])
                        else:
                            snakes[0].dir = i[2]
                        
                            snaketurn.append([0,i[2]])
                        

    screen.blit(eye1,(snakes[0].x + 10,snakes[0].y + 5))

    pblock.fill((255,255,255))
    screen.blit(pblock,(0,100))


    fruit1.update()
    died()
    pygame.display.update()

