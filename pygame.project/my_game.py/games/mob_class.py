import pygame
import os
import random
mob_seocond = 0
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images1")
class mob_class:
    def __init__(self, screen, mob_x,mob_y,mob_killed,mob_image_path,mob_seocond,mob_move_x,mob_move_y): #호출할때 이렇게쓰세요 / 변수 = mob(self,mob_x_pos,mob_y_pos,mob_killed,mob_image)
        #다 셀프로 변환시키기
        self.mob_x = mob_x
        self.mob_y = mob_y
        self.mob_killed = mob_killed
        self.mob_image_path = mob_image_path
        self.mob_seocond = mob_seocond
        self.mob_image = pygame.image.load(os.path.join(image_path,"test_mob.png"))
        self.mob_move_x = mob_move_x
        self.mob_move_y = mob_move_y
        self.screen = screen
        self.mob_rect = self.mob_image.get_rect()
        self.mob_rect.left = self.mob_x
        self.mob_rect.top = self.mob_y
    #랜덤 움직이기
    def process(self, chacracter_to_x, chacracter_to_y, deltaTime,mob):
        #안 죽었다면
        if self.mob_killed == 0:
            #(무한반복) mob_seocond에 20씩 더한다
            self.mob_seocond += 20
            #만약 mob_seocond 이 50000이라면
            if self.mob_seocond == 50000:
                #1부터8까지의 수중 한가지를랜덤으로골라 random_move에 넣는다
                self.random_move = random.randint(1, 8)
                #소수점 없에기
                self.random_move = int(self.random_move)
                if self.random_move == 1:
                    self.mob_move_y = 0.2    
                elif self.random_move == 2:
                    self.mob_move_x = 0.2
                elif self.random_move == 3:
                    self.mob_move_y = -0.2
                elif self.random_move == 4:
                    self.mob_move_x = -0.2
                elif self.random_move == 5:
                    self.mob_move_y = 0.25
                elif self.random_move == 6:
                    self.mob_move_x = 0.25
                elif self.random_move == 7:
                    self.mob_move_y = -0.25
                elif self.random_move == 8:
                    self.mob_move_x = -0.25
                self.mob_seocond = 0
            self.mob_x +=self.mob_move_x
            self.mob_y +=self.mob_move_y
            if self.mob_move_x > 0:
                self.mob_move_x = round(self.mob_move_x-0.0005,5)
            elif self.mob_move_x <0:
                self.mob_move_x =round(self.mob_move_x+0.0005,5)
            
            if self.mob_move_y > 0:
                self.mob_move_y= round(self.mob_move_y -0.0005,5)
            elif self.mob_move_y < 0:
                self.mob_move_y = round(self.mob_move_y+0.0005, 5)
            if  chacracter_to_x > 0:
                self.mobspd_x = 0.5
            else:
                self.mobspd_x = 0
            if chacracter_to_y > 0:
                self.mobspd_y = 0.5
                self.mobspd_y = 0
                
            self.mob_rect = self.mob_image.get_rect()
            self.mob_rect.left = self.mob_x
            self.mob_rect.top = self.mob_y

            self.mob_x += (-chacracter_to_x * deltaTime)
            self.mob_y += (-chacracter_to_y * deltaTime)
    def colliderect(self, object_rect):
        if(self.mob_rect.colliderect(object_rect)):
            self.mob_move_x = 0
            self.mob_move_y = 0
    def colliderect_cha(self,charater_rect):
        if self.mob_rect.colliderect(charater_rect):
            return True

    def update(self):
        self.screen.blit(self.mob_image,(self.mob_x, self.mob_y))
        border_color = (255,255,255)
        pygame.draw.rect(self.screen, border_color, self.mob_rect, width=2)

        
    