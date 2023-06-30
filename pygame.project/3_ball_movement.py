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

ball_images = [
    pygame.image.load(os.path.join(image_path,"ballon_1.png")),
    pygame.image.load(os.path.join(image_path,"ballon_2.png")),
    pygame.image.load(os.path.join(image_path,"ballon_3.png")),
    pygame.image.load(os.path.join(image_path,"ballon_4.png"))]



ball_speed_y = [-18,-15,-12,-9]

balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y":ball_speed_y[0]})

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


    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

    ball_size = ball_images[ball_img_idx].get_rect().size
    ball_width = ball_size[0]
    ball_hight = ball_size[1]
    
    if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
        ball_val["to_x"] = ball_val["to_x"]* -1



    if ball_pos_y >= screen_heght - stage_hight - ball_hight:
        ball_val["to_y"] = ball_val["init_spd_y"] 
    else:
        ball_val["to_y"] += 0.5
    ball_val["pos_x"] += ball_val["to_x"]
    ball_val["pos_y"] += ball_val["to_y"]

    screen.blit(backgrond,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    
    
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))
    screen.blit(stage,(0,screen_heght - stage_hight))
    screen.blit(chacracter,(chacracter_x_pos,chacracter_y_pos))
    
        
        
    
    
    
    pygame.display.update()




pygame.quit()



#https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=157s
#2:05:21 






















































































































































































"ㅋ"