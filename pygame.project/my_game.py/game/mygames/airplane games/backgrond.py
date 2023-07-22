import os
import pygame
from pygame.locals import *
import bar_class
import setting_class
import gamemenuclass
from pytmx import load_pygame
# 열거형 정의
class Scene():
    NoScene = 0
    StartScreen = 1
    Setting = 2
    Stage = 3

currentScene = Scene.StartScreen
nextScene = Scene.NoScene

nextScene = Scene.Setting
if nextScene != Scene.NoScene:
    # 화면 전환 효과

    # 다음 자면 정보 넘기기
    currentScene = nextScene
    nextScene = Scene.NoScene

if currentScene == Scene.Setting:
    currentScene = Scene.StartScreen


pygame.init()
pygame.mixer.init()
screen_width = 500
screen_heght = 900
image_path = "E:/siwoo/pygame.project/my_game.py/game/images"
ship_path = "E:/siwoo/pygame.project/my_game.py/game/images/ships"
screen = pygame.display.set_mode((screen_width,screen_heght))
pygame.display.set_caption("게임")
start_title = pygame.image.load(os.path.join(image_path,"background.png"))
start_title1 = pygame.image.load(os.path.join(image_path,"background.png"))
start_title3 = pygame.image.load(os.path.join(image_path,"background02.png"))
start_title4 = pygame.image.load(os.path.join(image_path,"background02.png"))
title = pygame.image.load(os.path.join(image_path,"title.png"))
setting = pygame.image.load(os.path.join(image_path,"setting.png"))
start_but = pygame.image.load(os.path.join(image_path,"startbut.png")).convert_alpha()
startxpos = 160
padding = 10
bars = []
font = pygame.font.Font(None, 36)
#soundbar = bar_class.bar( screen, 110, 100, 10, 7, 5, image_path)






menu = True
backgroundz = 0.0
backgroundz1 =490.0
backgroundz3 = 0.0
backgroundz4 = 635

first_esc = 0
setting_rect = setting.get_rect()
setting_rect.left = 145
setting_rect.top = 300
gamemenuT = False
a = 0
invis = 0
invis1 = 1
settingscene = setting_class.setting(screen, font, image_path)
settings = False
gamemenu = gamemenuclass.gamemenu(screen,image_path)
while menu:
    mousex,mousey = pygame.mouse.get_pos()
    if first_esc == 0:
        screen.blit(start_title1,(backgroundz1,0))
        screen.blit(start_title,(backgroundz,0))
        screen.blit(title,(245-200,300))
        screen.blit(start_title3,(backgroundz3,900-393))
        screen.blit(start_title4,(backgroundz4,900-393))
        screen.blit(start_but,(250-100,400))

        invis += invis1
        if invis == 255:
            invis1 = -1
        elif invis == 0:
            invis1 = 1
        start_but.set_alpha(invis)
        if backgroundz + 1019 == 0:
            backgroundz = 490

        if backgroundz1 + 1019== 0:
            backgroundz1 = 490
        
        if backgroundz3 + 635 == 0:
            backgroundz3 = 490 + (635 - 490)

        if backgroundz4 + 635 == 0:
            backgroundz4 = 490 + (635 - 490)

        backgroundz1 = round(backgroundz1 - 0.05, 3)
        backgroundz = round(backgroundz - 0.05,  3)
        backgroundz3 = round(backgroundz3 - 0.2, 3)
        backgroundz4 = round(backgroundz4 - 0.2, 3)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            setting == False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if first_esc == 0:                     
                    first_esc = 1
                else:
                    first_esc = 0
                
                
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if menu:
                if first_esc == 1:
                    if setting_rect.collidepoint(mousex,mousey):
                        settings = True
                        menu = False
                else:
                    gamemenuT = True


                
                

    if first_esc == 1:
        if menu:
            screen.blit(setting,(145,300))
    
    
    
    
    
    while gamemenuT:
        mousex,mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if gamemenu.ifpressed(event):
                gamemenuT = False
        
        gamemenu.update()
        pygame.display.update()
    
    
    
    
    while settings:

        mousex,mousey = pygame.mouse.get_pos()
        screen.fill((128,128,128))
        
        for screenbut in bars:
            screenbut.update(screen)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:

                settings = False
                
                menu == False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if settingscene.pressed(event,mousex,mousey) == True:
                    settings = False
                    menu = True
                    first_esc = 0


                
        settingscene.update()
        
        
        


        pygame.display.update()

    
    
    
    pygame.display.update()