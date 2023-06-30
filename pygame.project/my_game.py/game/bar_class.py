import pygame
from pygame.locals import *
import os

class bar:
    def __init__(self, _screen, _image_path):
        self.screen = _screen               # 화면 랜더링용 스크린
        self.image_path = _image_path
        self.isInit = False

    # def __init__(self, _screen, _startXPos, _startYPos, _maxVal, _initVal, _barPadding, _image_path):
        
    #     self.screen = _screen               # 화면 랜더링용 스크린
    #     self.image_path = _image_path
    #     self.initData(_startXPos, _startYPos, _maxVal, _initVal, _barPadding)

    #  초기값 설정
    def initData(self, _startXPos, _startYPos, _maxVal, _initVal, _barPadding):
        if self.isInit == True:
            return
        self.isInit = True
        
        self.startXPos = _startXPos          # 시작 X 좌표
        self.startYPos = _startYPos          # 시작 Y 좌표
        self.maxVal = _maxVal                # Bar의 최대 값
        self.currentVal = _initVal           # 현재 설정 값

        self.imageon = pygame.image.load(os.path.join(self.image_path,"bar_on.png"))
        self.imageoff = pygame.image.load(os.path.join(self.image_path,"bar_off.png"))
        self.rect = self.imageon.get_rect()


        self.barWidth = self.rect.width
        self.barHeight = self.rect.height
        self.barPadding = _barPadding
        self.barlist = []
        for i in range(1, self.maxVal+1):
            self.barlist.append(self.imageon.get_rect())


    # 버튼 처리용    
    def ifpressed(self,event,mousex,mousey):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for i in range(1,self.maxVal+1):
                if self.barlist[i-1].collidepoint(mousex,mousey):
                    self.currentVal = i
                    return True
        
        return False
            

                


    def update(self):
        for i in range(1,self.maxVal+1):
            tmpXPos = (((self.barPadding+self.barWidth)*(i-1))+self.startXPos)
            self.barlist[i-1].x = tmpXPos
            self.barlist[i-1].y = self.startYPos
            if i > self.currentVal:
                self.screen.blit(self.imageoff, (tmpXPos, self.startYPos))
                #self.barlist[i] = 
            else:
                self.screen.blit(self.imageon, (tmpXPos, self.startYPos) )
        
