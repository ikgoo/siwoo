import pygame
import time
import random
from enum import Enum

class GameState(Enum):
    MENU = 1        # 메뉴
    PLAY = 2        # 플레이
    GAMEOVER = 3    # 게임 오버

# 현재 상태 설정
current_state = GameState.PLAY

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 루프 변수
running = True

# FPS 설정
clock = pygame.time.Clock()
fps = 60  # 원하는 FPS 값 설정

moveCurrTime = 0      # 이동을 위한 시간 체크
moveStepTime = 0.1     # 뱀 이동 속도
snakeSize = 25         # 스네이크 크기
snakDir = 'D'         # 이동 방향 (W, A, S, D)
snakNextDir = 'D'     # 다음 이동한 방향
# 위치 정보 x,y(튜플)정보를 가지고 있는 리스트
snakes = []
snakImg = pygame.Surface((snakeSize, snakeSize))
snakImg.fill((255,255,255))

max_x = screen_width / snakeSize
max_y = screen_height / snakeSize

foodAddStep = 1         # 생성될 음식 수
foods = []             # 음식들 위치 정보
# 음식 이미지
foodImg = pygame.Surface((snakeSize, snakeSize))
foodImg.fill((0, 0, 0))  # 흰색 배경으로 채우기
circle_center = (snakeSize/2, snakeSize/2)  # 동그라미의 중심 좌표
circle_radius = snakeSize/2  # 동그라미의 반지름
circle_color = (255, 0, 0)  # 동그라미의 색상 (빨간색)
circle_thickness = 0  # 동그라미의 두께 (0: 채우기)
pygame.draw.circle(foodImg, circle_color, circle_center, circle_radius, circle_thickness)

def createFood():
    # 스테이크가 있는 자리인지 확인해서 제외
    while True:
        x = random.randint(0,  int(max_x))
        y = random.randint(0, int(max_y))
        chk = False
        for s in snakes:
            if x == s.x and y == s.y:
                chk = True

        if chk == False:        # 스네이크가 없는 위치면 음식을 추가
            foods.append((x, y))
            break


class snakebody:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 이동할 위치 계산
    def moveLoc(self):
        global snakDir  # 전역 변수로 선언
        global snakNextDir  # 전역 변수로 선언
        tmpx = self.x
        tmpy = self.y
        if snakNextDir == 'W':
            tmpy -= 1
        elif snakNextDir == 'S':
            tmpy += 1
        elif snakNextDir == 'A':
            tmpx -= 1
        elif snakNextDir == 'D':
            tmpx += 1        

        return (tmpx, tmpy)

    def proc(self):      # 충동 등 처리 확인(머리에서만 호출 됨)
        global snakes
        global current_state

        # 이동 후 처리
        tmpLoc = self.moveLoc()
        
        # 음식
        for f in foods:
            if f[0] == tmpLoc[0] and f[1] == tmpLoc[1]:       # 음식 충돌
                snakes.insert(0, snakebody(f[0], f[1]))
                foods.remove(f)
                createFood()
                return ''

        # 충돌(벽)
        for s in snakes:
            if s.x == tmpLoc[0] and s.y == tmpLoc[1]:
                current_state = GameState.GAMEOVER
                return ''    

        # 충돌(꼬리)
        if 0 > tmpLoc[0] or max_x < tmpLoc[0] or 0 > tmpLoc[1] or max_y < tmpLoc[1]:
            current_state = GameState.GAMEOVER
            return ''


        return 'NONE'
    
    
    # 머리 이동
    def moveHead(self):      # 이동 처리
        global snakDir  # 전역 변수로 선언
        global snakNextDir  # 전역 변수로 선언
        tmpLoc = self.moveLoc()
        self.x = tmpLoc[0]
        self.y = tmpLoc[1]
            
        if snakDir != snakNextDir:
            snakDir = snakNextDir
        
    # 꼬리 이동
    def moveNotHead(self, frontSnake):
        self.x = frontSnake.x
        self.y = frontSnake.y
        
    def update(self):
        global snakImg
        screen.blit(snakImg, (self.x * snakeSize, self.y * snakeSize))
        
    
# 시작 위치(10, 10)
for x in range(0, 3):
    snakes.append(snakebody(10-x, 10))

# 최초 음식 생성
createFood()

# 게임 루프
previous_time = time.time()  # 이전 프레임의 시간
while running:
    # 경과 시간 업데이트
    delta_time = clock.tick(fps) / 1000.0  # 경과 시간 계산 (초 단위)
    moveCurrTime += delta_time

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN and current_state == GameState.PLAY:        # 플레이 중일때 키입력
            if event.key == pygame.K_UP and snakDir != 'S':
                snakNextDir = 'W'
            elif event.key == pygame.K_DOWN and snakDir != 'W':
                snakNextDir = 'S'
            elif event.key == pygame.K_LEFT and snakDir != 'D':
                snakNextDir = 'A'
            elif event.key == pygame.K_RIGHT and snakDir != 'A':
                snakNextDir = 'D'


    if moveCurrTime >= moveStepTime:        # 지정된 시간 이후에 화면 랜더리 처리
        # 게임 로직 처리
        if current_state == GameState.MENU:
            pass
        elif current_state == GameState.PLAY:
            # 스네이크 그리기
            if moveCurrTime >= moveStepTime:
                moveCurrTime = moveCurrTime - moveStepTime
                tmpState = snakes[0].proc()
                if tmpState == 'NONE':          # 일반 이동 상태
                    for idx, s in enumerate(reversed(snakes)):
                        if idx == len(snakes)-1:
                            s.moveHead()
                        else:
                            s.moveNotHead(snakes[len(snakes)-1-idx-1])

                
        elif current_state == GameState.GAMEOVER:
            pass

        # 화면 그리기
        screen.fill((0, 0, 0))  # 검은색 배경

        # 화면 그림
        if current_state == GameState.MENU:
            pass
        elif current_state == GameState.PLAY or current_state == GameState.GAMEOVER:
            # 스네이크 그리기
            for s in snakes:
                s.update()

            # 음식 그리기
            for f in foods:
                screen.blit(foodImg, (f[0] * snakeSize, f[1] * snakeSize))
                
                
        if current_state == GameState.GAMEOVER:
            print('GAME OVER')

        pygame.display.update()

    # FPS 제어
    # clock.tick(fps)



# 게임 종료
pygame.quit()