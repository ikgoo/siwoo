to_x = 0
to_y = 0
a = 0



import os
import pygame
import random
##############################################
#기본 초기화(반트시 해야하는것)
pygame.init()
#화면 크기 설정
screen_width = 640
screen_heght = 480
screen = pygame.display.set_mode((screen_width,screen_heght))


#화면 타이틀
pygame.display .set_caption("nado pang")
#FPS
clock = pygame.time.Clock()
###################################################


current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")


backgrond = pygame.image.load(os.path.join(image_path, "backgrond.png"))


stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_hight = stage_size[1]

chacracter = pygame.image.load(os.path.join(image_path,"chareter.png"))
chacracter_size =chacracter.get_rect().size
chacracter_width = chacracter_size[0]
chacracter_hight = chacracter_size[1]
chacracter_x_pos = (screen_width  / 2 -(chacracter_width / 2))
chacracter_y_pos = screen_heght - chacracter_hight - stage_hight

chacracter_to = 0
chacracter_speed = 5

weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []

weapon_speed = 10



running = True
while running == True:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
        
        
            if event.key == pygame.K_LEFT:
                chacracter_to = -chacracter_speed
        
        
            elif event.key == pygame.K_RIGHT:
                chacracter_to = chacracter_speed
        
        
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = chacracter_x_pos + (chacracter_width / 2) - (weapon_width / 2)
                weapon_y_pos = chacracter_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                chacracter_to = 0
        
    
    chacracter_x_pos += chacracter_to
    
    if chacracter_x_pos < 0:
        chacracter_x_pos = 0
    elif chacracter_y_pos > screen_width - chacracter_width:
        chacracter_x_pos = screen_heght - chacracter_width
    weapons = [[w[0],w[1]- weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    screen.blit(backgrond,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    
    
    
    
    screen.blit(stage,(0,screen_heght - stage_hight))
    screen.blit(chacracter,(chacracter_x_pos,chacracter_y_pos))
    

        
        
    
    
    
    pygame.display.update()




pygame.quit()



#https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=157s
#1:43:15
