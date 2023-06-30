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
###############################################


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

a = 0

ball_speed_y = [-17,-15,-12,-9]

balls = []

balls.append({
    "pos_x" : 30,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 2,
    "to_y" : -6,
    "init_spd_y":ball_speed_y[0]
    
   
    })

weapon_to_remove = -1
ball_to_remove = -1
#폰트
game_font = pygame.font.Font(None, 40) #game_font = pygame.font.Font(무조건 None,글자크기) 게임폰트 만들기


#시간
total_time = 100 #총시간

start_ticks = pygame.time.get_ticks() #시작 시간 정의


#게임끝/ TimeOut , Mission Complete , Game Over (시간초과,공을 다 터트림,공에 맞음)
game_result = "Game Over" #글자



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
    elif chacracter_x_pos > screen_width - chacracter_width:
        chacracter_x_pos = screen_width - chacracter_width
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

    
    
        chacracter_rect = chacracter.get_rect()
        chacracter_rect.left = chacracter_x_pos
        chacracter_rect.top = chacracter_y_pos
    
     


        
        
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y


        if chacracter_rect.colliderect(ball_rect):
            running = False
            a = 1
            break

        
        
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

        
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            
            
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx
                
                if ball_img_idx < 3:
                    
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]


                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    
                    
                    
                    
                    
                    #오른쪽공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) -(small_ball_width/2),
                        "pos_y" : ball_pos_y + (ball_height / 2) -(small_ball_height/2),
                        "img_idx" : ball_img_idx +1,
                        "to_x" : 3,
                        "to_y" : -6,
                        "init_spd_y":ball_speed_y[ball_img_idx + 1]})
                    #왼쪽공
                    
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx +1,
                        "to_x" : -3,
                        "to_y" : -6,
                        "init_spd_y":ball_speed_y[ball_img_idx + 1]})
                
                        
                break



        
        
        
        
            if ball_to_remove > -1:
                del balls[ball_to_remove]
                ball_to_remove = -1


            
            
            if weapon_to_remove > -1:
                del weapons[weapon_to_remove]
                weapon_to_remove = -1


            if len(balls) == 0: #만야 공이 없다면(0개라면)
                game_result = "Mission Complete" #미션성공을 뜨게한다
                running = False #게임 멈추기
                a = 1
            

    
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
    

    #경과된 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드(ms)에서 초(s)로 바꾸는 것
    timer = game_font.render("Time : {0}".format(int(total_time - elapsed_time )),True ,(255,255,255)) #game_font.render / int는 소수점단위를 안보일려고 100(total_time) - 경과된시간(elapsed_time) = 시간이 거꾸로감 / (무조건 True,(색 #255,255,255 = 흰색))
    screen.blit(timer,(10,10)) #screen.blit( str아니면int의 변수 , (위치 x , y))
    



    #시간초과
    if total_time - elapsed_time <= 0:  #100 - 경과된시간이 0보다 작거나 같다면
        game_result = "Time Out"        #게임이 왜 끝났는지의 이유(게임 결과) 를 시간초과로 바꿈
        running = False  
        a = 1          #게임 멈추기



    



    pygame.display.update()



#게임오버 메시지
if a >= 1:
    msg = game_font.render(game_result,True,(255,255,0)) #255,255,0 = 노랑
    msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_heght / 2))) #center = 화면의 맨 오른쪽 나누기 2 = (x좌표정중앙) 화면의 맨위 나누기 2 = (y좌표 정중앙) int = 소수점 제거
    screen.blit(msg,msg_rect) #메세지를 뜨게한다 msg_rect(화면 정중앙)에
    pygame.display.update()
    pygame.time.delay(2000)  #게임오버 메세지 업데이트

#2초 기다리기



pygame.quit()



#https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=157s
#2:42:18
 
