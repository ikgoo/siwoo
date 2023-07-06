import pygame
import time
import random


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# https://firebase.google.com/docs/firestore/query-data/get-data?hl=ko#python
# https://firebase.google.com/docs/firestore/manage-data/add-data?hl=ko
cred = credentials.Certificate("siwoo-b39ff-firebase-admin.json")
firebase_admin.initialize_app(cred)

moveCurrTime = 0
db = firestore.client()



gameRankDataObj = db.collection("game").document("ranking")    
gameRankData = gameRankDataObj.get().to_dict()                 



gameRankDataObj.set(gameRankData)

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
        self.snakeb.fill((color[colornum -1 ][1]))
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
        global snx
        global sny
        hibr = self.hitbox.get_rect()
        hibr.left = self.x - 2.5
        hibr.top = self.y-2.5

        if hibr.colliderect(snakehitbox):
            self.point += 1
            for c in snakes:
                c.ownnum = c.ownnum + 1
            if snakes[0].dir == "up":
                snakes.insert(0,snakebod(snakes[0].x,snakes[0].y - 25,1))
            elif snakes[0].dir == "down":
                snakes.insert(0,snakebod(snakes[0].x,snakes[0].y + 25,1))
            elif snakes[0].dir == "left":
                snakes.insert(0,snakebod(snakes[0].x - 25,snakes[0].y,1))
            elif snakes[0].dir == "right":
                snakes.insert(0,snakebod(snakes[0].x + 25,snakes[0].y,1))
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



msnaketurn = []
eye1 = pygame.Surface((10,10))
eye2 = pygame.Surface((10,10))
cene = 0
game = True
fruit1.sum()
menu = True
msnakes = []
on = True
arrownum = 1
fs = 1
colornum = 0
color = [["white",(255,255,255)],["Red",(255,0,0)],["Blue",(0,0,255)],["Green",(0,200,0)],["Black",(0,0,0)]]

while on:
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
    
    pblock = pygame.Surface((700,10))
    fruit1 = fruit()
    snakes = []



    msnaketurn = []
    eye1 = pygame.Surface((10,10))
    eye2 = pygame.Surface((10,10))
    cene = 0
    game = True
    fruit1.sum()
    menu = True
    msnakes = []
    on = True
    arrownum = 1
    fs = 1
    colornum = 0
    color = [["white",(255,255,255)],["Red",(255,0,0)],["Blue",(0,0,255)],["Green",(0,200,0)],["Black",(0,0,0)]]
    for s in range(1,4):
        snakes.append(snakebod(350 - s * 25 + 1,350+1,s))
    for s in range(1,4):
        msnakes.append(snakebod(400 - s * 25 + 1,350+1,s))
    while menu:



        screen.fill((0,0,0))
        pygame.draw.rect(screen,(100,200,0),(0,100,700,600))
        for i in range(28):

            line1  = pygame.draw.line(screen,(0,255,0) ,(0,100 + i * 25),(700,100 + i * 25),width=10)

            line2 = pygame.draw.line(screen,(0,255,0) ,(0 + i * 25,100),(0 + i * 25,700),width=10)

        pblock.fill((255,255,255))
        screen.blit(pblock,(0,100))

        time.sleep(0.5)
        






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rankf = []
                    print(gameRankData)

                    sortedv = sorted(gameRankData.items(), key=lambda x: x[1], reverse=True)


                    ranked = []
                    for i, (key, value) in enumerate(sortedv):
                        ranked.append({"이름": key, "점수": value, "랭킹": i+1})


                    for person in ranked:
                        rankf.append(font.render(f"{person['랭킹']}: {person['이름']} {person['점수']}point",True,(255,255,255)))

                    for i in rankf:
                        i = pygame.transform.scale(i,(280,50))
                    rankingT = True
                    while rankingT:
                        ford = 0
                        for i in rankf:
                            screen.blit(i,(0,100+ford * 50))
                            ford += 1
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    rankingT = False
                                    
                        pygame.display.update()

                        


                        

                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    menu = False
                    game = True

                if event.key == pygame.K_t:



                    seting = True
                    while seting:
                        screen.fill((255,255,255))

                        speed = ["fast","normal","slow"]

                        arrow = font.render(">",True,(0,0,0))


                        modesp = font.render("speed : " + speed[fs],True,(0,200,0))
                        mode = font.render("press arrow to next",True,(0,0,200))
                        mode2 = font.render("press space to change modes",True,(0,0,200))
                        setingt = font.render("setting",True,(128,128,128))
                        esc = font.render("press esc to out",True,(200,0,0))
                        for a in color:

                            if colornum == color.index(a):
                                modesnc = font.render("snake color : " + a[0],True,(0,200,0))
                        mode = pygame.transform.scale(mode,(300,70))
                        setingt = pygame.transform.scale(setingt,(250,70))
                        modesp = pygame.transform.scale(modesp,(250,70))
                        arrow = pygame.transform.scale(arrow,(50,50))
                        modesnc = pygame.transform.scale(modesnc,(280,70))
                        mode2 = pygame.transform.scale(mode2,(400,70))
                        esc = pygame.transform.scale(esc,(280,70))
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                    arrownum = 1
                                if event.key == pygame.K_DOWN:
                                    arrownum = 2
                                if event.key == pygame.K_SPACE:
                                    if arrownum == 1:
                                        if fs != 2:
                                            fs += 1
                                        else:
                                            fs = 0
                                    else:
                                        if colornum != 4:
                                            colornum += 1
                                        else:
                                            colornum = 0
                                if event.key == pygame.K_ESCAPE:
                                    seting = False
                                    for i in snakes:
                                        i.snakeb.fill((color[colornum - 1][1]))
                        screen.blit(mode,(350 - 150,200))

                        screen.blit(arrow,(350 - 200,300 + 100 * (arrownum - 1)))
                        
                        screen.blit(modesp,(350 - 125,300))
                        screen.blit(setingt,(350 -125,50))
                        screen.blit(modesnc,(350 -125,400))
                        screen.blit(mode2,(350-200,120))
                        screen.blit(esc,(350 - 140,600))
                        pygame.display.update()

        
        for x in msnakes:

            x.update()
        pygame.display.update()
        msnake = pygame.Surface((75,25))
        msnake.fill((255,255,255))
        screen.blit(msnake,(323,347))
        snake_game = font.render("SNAKE GAME",True,(0,0,0))
        enter = font.render("press enter to start",True,(255,255,255))
        enter = pygame.transform.scale(enter,(250,50))
        set = font.render("press t to setting",True,(255,255,255))
        rank = font.render("press r to ranking",True,(255,255,255))
        set = pygame.transform.scale(set,(250,50))
        rank = pygame.transform.scale(rank,(250,50))
        screen.blit(enter,(350 - 125,450))
        screen.blit(rank,(350-125,550))
        screen.blit(snake_game,(150,200))
        screen.blit(set,(350 - 125,500))
        screen.blit(eye2,(325 + 10,350 + 5))
        pygame.display.update()
        
        pygame.display.update()

            
    key = 0
    def died():
        global game
        global sr
        global screen
        global menu
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
                        x.fall += round(0.002,4)
                        x.update()
                        if index == 0:
                            screen.blit(eye1,(snakes[0].x + 10,snakes[0].y+5))
                        pygame.display.update()
                        done1 = False
                arrw = 1
                rank = True
                while rank:
                    rankok = font.render("Do you want to put your score on the ranking?",True,(0,0,0))
                    screen.fill((255,255,255))
                    ox = font.render("o       x",True,(0,0,0))
                    arr = font.render(" /\ ",True,(0,0,0))
                    arr = pygame.transform.scale(arr,(80,100))
                    ox = pygame.transform.scale(ox,(400,70))
                    rankok = pygame.transform.scale(rankok,(700,70))
                    
                    done = False
                    screen.blit(ox,(350 - 200,300))
                    screen.blit(rankok,(0,100))
                    if arrw == 1:
                        screen.blit(arr,(150 + 15.5 - 10,450))
                    elif arrw == 2:
                        screen.blit(arr,(450 + 15.5 - 10,450))

                    
                    
                    name = ""
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                arrw = 1
                            if event.key == pygame.K_RIGHT:
                                arrw = 2
                            if event.key == pygame.K_SPACE:
                                if arrw == 2:
                                    rank = False
                                if arrw == 1:
                                
                                    rankT = True
                                    while rankT:

                                        screen.fill((255,255,255))
                                        namet = font.render(name,True,(0,0,0))
                                        inp = font.render("put your name",True,(0,0,0))
                                        inp = pygame.transform.scale(inp,(280,70))
                                        




                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                running = False
                                            elif event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_RETURN:

                                                    done = True
                                                    break
                                                elif event.key == pygame.K_BACKSPACE:

                                                    name = name[:-1]
                                                else:

                                                    name += event.unicode
                                        screen.blit(namet,(0,600))
                                        
                                        screen.blit(inp,(350-140,200))
                                        pygame.display.update()
                                        if done == True:

                                            gameRankData[name] =fruit1.point
                                            gameRankDataObj.set(gameRankData)
                                            if len(gameRankData) >= 11:
                                                ranked.pop(10)

                                            done1 = True
                                        
                                        if done1 == True:
                                            rankT = False
                                            rank = False
                                game = False
                                menu = True

                                break
                            # gameover = pygame.font.render("game over", True, (255,0,50))
                    
                    # pygame.display.update()
                            
    previous_time = 0
    while game:
        current_time = time.time()
        delta_time = current_time - previous_time
        previous_time = current_time
        moveCurrTime += delta_time
        hitbox()



        screen.fill((0,0,0))
        


        for x in snaketurn:
            if moveCurrTime >= 0.1:
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
                

        pygame.draw.rect(screen,(100,200,0),(0,100,700,600))

        for i in range(28):
            pygame.draw.line(screen,(0,255,0) ,(0,100 + i * 25),(700,100 + i * 25),width=10)
            pygame.draw.line(screen,(0,255,0) ,(0 + i * 25,100),(0 + i * 25,700),width=10)

        for i in snakes:
            i.snakeb.fill(color[colornum][1])
            if getped == 0:
                if key == 1:
                    if fs == 0:
                        if moveCurrTime >= 0.09:
                            if getped == 0:
                                i.go()
                    else:
                        if moveCurrTime >= fs / 10:
                            if getped == 0:
                                i.go()
                            
                        
                    i.update()
                i.update()
            i.update()
        if fs == 0:
            
            if moveCurrTime >= 0.09:
                moveCurrTime = 0
            else:
                if moveCurrTime >= fs / 10:
                    moveCurrTime = 0
            getped = 0
        

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                key = 1
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

        if fruit1.getp():
            getped =1
            fruit1.sum()
        pygame.display.update()
        
