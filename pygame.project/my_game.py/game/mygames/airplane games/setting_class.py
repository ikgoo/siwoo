import bar_class
import onoff
import pygame
from pygame.locals import *
import butten
import os

class setting:

    def __init__(self, screen, font, image_path):
        self.screen = screen
        self.font = font
        self.image_path = image_path
        self.bars = []
        self.settingBase = [
            ['Sound Volum', 'Bar', bar_class.bar(screen, image_path)],
            ['Blaster', 'OnOff', onoff.onoffclass(self.screen,self.image_path)],
        ]
        self.settingVal = [5, 1]

        self.startXPos = 50
        self.startYPos = 100
        self.labelWidth = 150
        self.xPadding = 30
        self.labelHight = 30
        self.yPadding = 100
        self.labels = [0,1]
        on = pygame.image.load(os.path.join(self.image_path,"red_button06_back.png"))
        self.outbut = butten.buttens(on,300,800,self.screen)
        
    def update(self):
        self.screen.fill((128,128,128))

            


        for i in range(1, len(self.settingBase)+1):
            #label 그리기
            # self.settingBase[i-1][2].initData(110, 100, 10, 7, 5)
            tmpyPos = self.startYPos + (self.yPadding * (i-1))
            tmpxsettingpos = self.startXPos + self.labelWidth + self.xPadding
            self.screen.blit((self.font.render(self.settingBase[i-1][0],True,(255,255,255))), (self.startXPos,tmpyPos))

            #설정 그리기
            if self.settingBase[i-1][1] == 'Bar':
                self.settingBase[i-1][2].initData(tmpxsettingpos, tmpyPos, 10, 7, 5)
                
                self.settingBase[i-1][2].update()
            elif(self.settingBase[i-1][1] == 'OnOff'):
                self.settingBase[i-1][2].init(tmpxsettingpos,tmpyPos)
                self.settingBase[i-1][2].update()
        self.outbut.update()
        

    def pressed(self,event,mousex,mousey):
        for i in range(1, len(self.settingBase)+1):
            chkYn = self.settingBase[i-1][2].ifpressed(event,mousex,mousey)
            if chkYn == True: 
                return False

        chkYn = self.outbut.ifpressed(event,mousex,mousey)
        if chkYn == True:
            # 메인 화면으로 이동하는 로직이 필요
            return True
        
        # if self.outbut.update() == True:
        #     return False
        # else:
        #     return True

