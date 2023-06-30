import pygame
import os
import random
import mob_class
################################
pygame.init()
pygame.mixer.init()

sreen_width = 640
screen_heght = 480

screen = pygame.display.set_mode((sreen_width,screen_heght))

pygame.display .set_caption("어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메의문단속,포켓몬스터콜라보레이션150인치LG초고화질접이식리미티드에디션1억짜리티비어쩔티비 프리미엄 슈퍼 리미티드 짱짱 최고 이세상에 1개인 울트라 슈퍼 1초만에 세탁이 끝나는 정말좋은 슈퍼 리미티드 삼상과 레드핑크의 콜라보 레이션 단돈100조원티비어쩔뽀로로,헬로카봇,또봇,시크릿쥬쥬,스즈메 ")
####################################

mob_killed = 0

no_mob = 0

walk = 0

mob_seocond = 0

mob_x = 600
mob_y = 300

mob_move_x = 0
mob_move_y = 0

k_up = True

chacracter_to_y = 0

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images1")
sound_path = os.path.join(current_path,"sounds")

test = -1

ani_speed = 0.005

mo_mob = 0

chacracter_x_pos = 0
chacracter_y_pos = 0

fence_left_x = 360
fence_left_y = 170

fence_up_x = 365
fence_up_y = 170

fence_down_x = 365
fence_down_y = 1100

fence_right_x = 1320
fence_right_y = 170

def do_something_else():
    # 다른 작업 수행
    pass
char_right = [
    pygame.image.load(os.path.join(image_path,"run_0.png")),
    pygame.image.load(os.path.join(image_path,"run_1.png")),
    pygame.image.load(os.path.join(image_path,"run_2.png")),
    pygame.image.load(os.path.join(image_path,"run_3.png")),
    pygame.image.load(os.path.join(image_path,"run_4.png")),
    pygame.image.load(os.path.join(image_path,"run_5.png")),
]
charater = pygame.image.load(os.path.join(image_path,"run_0.png"))

charater_to = 0

screen.blit(charater,(0,0))

chacracter_speed = 0.2

backgrond = pygame.image.load(os.path.join(image_path,"backgrond.png"))

running = True

mob = pygame.image.load(os.path.join(image_path,"test_mob.png"))
screen.blit(mob,(800,500))

expree = pygame.image.load(os.path.join(image_path,"!.png"))

walk_pose = 0

chacracter_to_x = 0
charater_to_y = 0

flip_x = False

keydownleftright = 0

mobspd_x = 0
mobspd_y = 0
a = 0
game_font = pygame.font.Font(None,36)
gofights = [
    pygame.image.load(os.path.join(image_path,"gofight1.png")),
    pygame.image.load(os.path.join(image_path,"gofight2.png")),
    pygame.image.load(os.path.join(image_path,"gofight3.png")),
    pygame.image.load(os.path.join(image_path,"gofight4.png")),
]
#startTime = pygame.time.Clock()
start_ticks = pygame.time.get_ticks() #시작 시간 정의
deltaTime = 0.0

ishit = False

fence_left = pygame.image.load(os.path.join(image_path,"long_fence_up_left.png"))
fence_right = pygame.image.load(os.path.join(image_path,"long_fence_up_right.png"))
fence_up = pygame.image.load(os.path.join(image_path,"long_fence_up_up.png"))
fence_down = pygame.image.load(os.path.join(image_path,"long_fence_up_up.png"))

sound = pygame.mixer.Sound('E:\siwoo\pygame.project\my_game.py\sounds/0_angel_waltz_180.ogg') #소리

gofight_size = pygame.image.load(os.path.join(image_path,"gofight_size.png"))

gofight_size_x = 800
gofight_size_y = 800




### 충돌 정의
def mob_hit_effect(delay_time,delay_time_expree):
    global gofight_size
    global gofight_size_y
    global gofight_size_x
    screen.blit(expree,(280,200))
    pygame.display.update()
    pygame.time.delay(delay_time_expree)
    for test in range(1000000):
        gofight_size = pygame.transform.scale(gofight_size,(gofight_size_x,gofight_size_y))
        gofight_size_x -= 1
        gofight_size_y -= 1
        screen.blit(backgrond,(0,0))
        screen.blit(mob,(mob_x ,mob_y))
        screen.blit(charater,(250,170))
        screen.blit(fence_left,(fence_left_x,fence_left_y))
        screen.blit(fence_up,(fence_up_x,fence_up_y))
        screen.blit(fence_down,(fence_down_x,fence_down_y))
        screen.blit(fence_right,(fence_right_x,fence_right_y))
        screen.blit(gofight_size,(0 ,0))
        if gofight_size_x == 0 or gofight_size_y == 0:
            break
        pygame.display.update()
        

mob_image = os.path.join(image_path,"test_mob.png")
mob1 = mob_class.mob_class(screen,600,300,False,mob_image,0,0,0)


def fighting(charater,mob,charater_dam1,charater_dam2,mob_dam,charater_skills1,charater_skills2,mob_HP,charater_HP,mob_name):
    global running
    global no_mob
    global mob_killed
    global sound
    no_fast_space = 0
    charater = pygame.transform.flip(char_right[walk_pose], False, False)
    pygame.display.update()
    fighting = True
    aroow1 = 0
    aroow2 = 0
    while fighting == True:
        if no_fast_space == 0:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fighting = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if aroow1 != 1:
                            aroow1 = 1
                            aroow2 = 1
                    if event.key == pygame.K_UP:
                        if aroow2 != 1:
                            continue
                        elif aroow2 == 1:
                            aroow1 = 0
                            aroow2 = 0
                    if event.key == pygame.K_SPACE:
                        no_fast_space = 1
                        
                        if aroow1 == 0:
                            aroow1 = -1
                            aroow2 = -1
                            no_fast_space = 1
                            charater = pygame.image.load(os.path.join(image_path,"kimchi ssadagu_0.png"))
                            charater = pygame.transform.scale(charater,(140,100))
                            screen.blit(backgrond,(0,0))
                            screen.blit(charater,(50,300))
                            screen.blit(mob,(550,130))
                            pygame.display.update()
                            pygame.time.delay(500)
                            hurt = pygame.image.load(os.path.join(image_path,"hurt.png"))
                            screen.blit(backgrond,(0,0))
                            screen.blit(charater,(50,300))
                            screen.blit(mob,(550,130))
                            screen.blit(hurt,(550,130))
                            pygame.display.update()
                            pygame.time.delay(500)
                            charater = pygame.image.load(os.path.join(image_path,"run_0.png"))
                            mob_HP -= charater_dam1
                            aroow1 = 0
                            aroow2 = 0
                            no_fast_space = 0
                        if aroow1 == 1:
                            
                            aroow1 = -1
                            aroow2 = -1
                            charater = pygame.image.load(os.path.join(image_path,"attack_0[1].png"))
                            charater = pygame.transform.scale(charater,(140,100))
                            screen.blit(backgrond,(0,0))
                            screen.blit(charater,(50,300))
                            screen.blit(mob,(550,130))
                            pygame.display.update()
                            pygame.time.delay(500)
                            hurt = pygame.image.load(os.path.join(image_path,"hurt.png"))
                            screen.blit(backgrond,(0,0))
                            screen.blit(charater,(50,300))
                            screen.blit(mob,(550,130))
                            screen.blit(hurt,(550,130))
                            pygame.display.update()
                            pygame.time.delay(500)
                            charater = pygame.image.load(os.path.join(image_path,"run_0.png"))
                            mob_HP -= charater_dam2
                            aroow1 = 1
                            aroow2 = 1
                            no_fast_space = 0
                            
                        
                        pygame.event.clear()

        if mob_HP <= 0:
            winning = game_font.render("win",True,(255,255,255))
            winning_font = winning.get_rect()
            winning_font.center = (320, 240)
            screen.blit(winning,winning_font)
            pygame.display.update()
            pygame.time.delay(3000)
            fighting = False
            mob_killed = 1
            no_mob = 1
        if aroow1 == 0:
            skills1 = game_font.render(">{0} damage:{1}".format(charater_skills1,charater_dam1),True,(255,255,255))
        else:
            skills1 = game_font.render("{0} damage:{1}".format(charater_skills1,charater_dam1),True,(255,255,255))
        if aroow2 == 1:
            skills2 = game_font.render(">{0} damage:{1}".format(charater_skills2,charater_dam2),True,(255,255,255))
        else:
            skills2 = game_font.render("{0} damage:{1}".format(charater_skills2,charater_dam2),True,(255,255,255))
        
        mob_name_for_font = game_font.render(mob_name,True,(255,255,255))
        mob_HP_for_font = game_font.render("HP :" + str(mob_HP),True,(255,255,255))
        mob_name_font = mob_name_for_font.get_rect()
        skill1_font = skills1.get_rect()
        skill2_font = skills2.get_rect()
        mob_HP_font = mob_HP_for_font.get_rect()

        skill1_font.center = (200,400)
        skill2_font.center = (200,450)
        mob_name_font.center = (500,120)
        mob_HP_font.center = (500,100)

        screen.blit(backgrond,(0,0))
        charater = pygame.transform.scale(charater,(140,100))
        screen.blit(charater,(50,300))
        screen.blit(mob,(500,130))
        screen.blit(skills1,skill1_font)
        screen.blit(skills2,skill2_font)
        screen.blit(mob_name_for_font,(mob_name_font))
        screen.blit(mob_HP_for_font,(mob_HP_font))
        
        
        
        
        
        
        
        pygame.display.update()

quit = 0 #게임나가는 변수

pygame.mixer.music.load(os.path.join(sound_path,"0_angel_waltz_180.ogg"))
pygame.mixer.music.play()
endevent = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(endevent)

while running == True:
    
    deltaTime = pygame.time.get_ticks() - start_ticks
    start_ticks = pygame.time.get_ticks()

    #process 처리 : Start
    mob1.process(chacracter_to_x,chacracter_to_y,deltaTime,mob)

    #process 처리 : End

    #update 처리 : Start

    #update 처리 : End
    

    first_backgrond_sound = sound.play
    #print(deltaTime)
    if test < 0:
        for event in pygame.event.get():
            if event.type == endevent:
                # "음악 종료 이벤트"가 발생하면 다시 처음부터 노래를 재생합니다.
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()
            if event.type == pygame.QUIT:
                # running = False
                # quit = 1
                print("나보다 약한자따위의말은듣지않는다,끄기")

            if event.type == pygame.KEYDOWN:
                k_up = False
                if event.key == pygame.K_LEFT:
                    print("나보다 약한자따위의말은듣지않는다,아래로가기")
                if event.key == pygame.K_RIGHT:
                    
                    print("나보다 약한자따위의말은듣지않는다,오른쪽으로가기")
                if event.key == pygame.K_UP:
                    print("나보다 약한자따위의말은듣지않는다,위로가기")

                if event.key == pygame.K_DOWN:
                    print("나보다 약한자따위의말은듣지않는다,왼쪽으로가기")
                    
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    chacracter_to_x = 0
            
                if event.key == pygame.K_RIGHT:
                    chacracter_to_x = 0

                if event.key == pygame.K_UP:
                    chacracter_to_y = 0
    
                if event.key == pygame.K_DOWN:
                    chacracter_to_y = 0

    mob_rect = mob.get_rect()
    mob_rect.left = mob_x
    mob_rect.top = mob_y
    charater_rect = charater.get_rect()
    charater_rect.left = 250
    charater_rect.top = 170
    charater_rect = charater_rect.inflate(-60,-17)
    charater_rect = charater_rect.move(-10,0)
    
    fence_up_rect = fence_up.get_rect()
    fence_up_rect.left = fence_up_x
    fence_up_rect.top = fence_up_y
    
    fence_down_rect = fence_down.get_rect()
    fence_down_rect.left = fence_down_x
    fence_down_rect.top = fence_down_y
    
    fence_right_rect = fence_right.get_rect()
    fence_right_rect.left = fence_right_x
    fence_right_rect.top = fence_right_y
    
    fence_left_rect = fence_left.get_rect()
    fence_left_rect.left = fence_left_x
    fence_left_rect.top = fence_left_y

    no_down = 0
    no_left = 0
    no_right = 0

    # if charater_rect.colliderect(fence_left_rect): #울타리에 캐릭터가 막히게하기
    #     if chacracter_to_x > 0:
    #         chacracter_to_x = 0
    # if charater_rect.colliderect(fence_up_rect):
    #     if chacracter_to_y > 0:
    #         chacracter_to_y = 0
    # if charater_rect.colliderect(fence_right_rect):
    #     if chacracter_to_x < 0:
    #         chacracter_to_x = 0
    # if charater_rect.colliderect(fence_down_rect):
    #     if chacracter_to_y < 0:
    #         chacracter_to_y = 0
    
    # if mob1.colliderect(fence_left_rect):
    #     if mob1.mob_move_x < 0:
    #         mob1.mob_move_x = 0
    # if mob1.colliderect(fence_up_rect):
    #     if mob1.mob_move_y > 0:
    #         mob1.mob_move_y = 0
    # if mob1.colliderect(fence_down_rect):
    #     if mob1.mob_move_y > 0:
    #         mob1.mob_move_y = 0
    # if mob1.colliderect(fence_right_rect):
    #     if mob1.mob_move_x > 0:
    #         mob1.mob_move_y = 0            
    # if mob_rect.colliderect(fence_left_rect): #울타리 몹막히기
    #     if mob_move_x < 0:
    #         mob_move_x = 0
    if mob_rect.colliderect(fence_up_rect):
        if mob_move_y < 0:
            mob_move_y = 0
    if mob_rect.colliderect(fence_right_rect):
        if mob_move_x > 0:
            mob_move_x = 0
    if mob_rect.colliderect(fence_down_rect):
        if mob_move_y > 0:
            mob_move_y = 0

    
    
    if chacracter_to_x != 0 or chacracter_to_y != 0:
        walk_pose = int(a)
    else:
        walk_pose = 0
    if a >= 5:
        a = 0
        walk_pose = 0

    if k_up == False:
            walk += 20
            a = a+(ani_speed * deltaTime)

    chacracter_x_pos += (chacracter_to_x * deltaTime)
    chacracter_y_pos += (chacracter_to_y * deltaTime)

    charater = char_right[walk_pose]
    #print(mob_seocond)

    # print(mob_move_x)
    if chacracter_to_x == 0.2:
        flip_x = False
    elif chacracter_to_x == -0.2:
        flip_x = True
    if  chacracter_to_x > 0:
        mobspd_x = 0.5
    else:
        mobspd_x = 0
    if chacracter_to_y > 0:
        mobspd_y = 0.5
    else:
        mobspd_y = 0

    charater = pygame.transform.flip(char_right[walk_pose], flip_x, False)
    charater = pygame.transform.scale(charater,(140,100))
    gofights[0] = pygame.transform.scale(gofights[0],(640,480))
    gofights[1] = pygame.transform.scale(gofights[1],(640,480))
    gofights[2] = pygame.transform.scale(gofights[2],(640,480))
    gofights[3] = pygame.transform.scale(gofights[3],(640,480))
    backgrond = pygame.transform.scale(backgrond,(640,480))
    fence_left = pygame.transform.scale(fence_left,(50,1000))
    fence_right = pygame.transform.scale(fence_right,(50,1000))
    fence_up = pygame.transform.scale(fence_up,(1000,80))
    fence_down = pygame.transform.scale(fence_down,(1000,80))
    # if mob_x >= 640 or mob_y >= 400:
    #     mob_x = 400
    #     mob_y = 200
    mob_x += (-chacracter_to_x * deltaTime)
    mob_y += (-chacracter_to_y * deltaTime)
    fence_left_x += (-chacracter_to_x * deltaTime)
    fence_left_y += (-chacracter_to_y * deltaTime)
    fence_up_x += (-chacracter_to_x * deltaTime)
    fence_up_y += (-chacracter_to_y * deltaTime)
    fence_down_x += (-chacracter_to_x * deltaTime)
    fence_down_y += (-chacracter_to_y * deltaTime)
    fence_right_x += (-chacracter_to_x * deltaTime)
    fence_right_y += (-chacracter_to_y * deltaTime)
    if ishit == False and charater_rect.colliderect(mob_rect):
        ishit = True
        start_ticks = pygame.time.get_ticks()
        mob_hit_effect(100,2000)     # 충돌 효과
        fighting(charater,mob,5,10,5,"Kimchi ssadagu","fakt ppokkuck",30,10,"The black dark Legendery the bilter of the god")
        chacracter_to_x = 0
        chacracter_to_y = 0


    
    
    
    screen.blit(backgrond,(0 ,0))
    
    if no_mob == 0:
        mob1.update()
        # screen.blit(mob1,(mob_x ,mob_y))
    screen.blit(charater,(250,170))
    screen.blit(fence_left,(fence_left_x,fence_left_y))
    screen.blit(fence_up,(fence_up_x,fence_up_y))
    screen.blit(fence_down,(fence_down_x,fence_down_y))
    screen.blit(fence_right,(fence_right_x,fence_right_y))
    border_color = (255, 255, 255)  # 흰색
    pygame.draw.rect(screen, border_color, mob_rect, width=2)  # 테두리 그리기
    pygame.draw.rect(screen, border_color, charater_rect, width=2)  # 테두리 그리기
    mob1.update()
    if quit == 1:
        break
    

    pygame.display.update()



#C:\Users\twopro\My project\Assets\GigaPack















