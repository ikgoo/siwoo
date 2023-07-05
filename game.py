import pygame
import time

from PIL import Image, ImageFilter

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Image.open

# 게임 루프 변수
running = True

pygame.transform.smoothscale

moveCurrTime = 0		# 이동을 위한 시간 체크
moveStepTime = 0.1		# 1초에 한간
snakeSize = 25    		# 스네이크 크기
snakDir = 'D'			# 이동 방향 (W, A, S, D)
snakNextDir = 'D'

class snakebody:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.snakeb = pygame.Surface((snakeSize, snakeSize))
        self.snakeb.fill((255,255,255))
        self.moveKeys = []
    
    def proc(self):		# 충동 등 처리 확인
        pass
    
    def appendKye(self, key):
        self.moveKeys.append(key)
    
    def moveHead(self):		# 이동 처리
        if snakNextDir == 'W':
            self.y -= 1
        elif snakNextDir == 'S':
            self.y += 1
        elif snakNextDir == 'A':
            self.x -= 1
        elif snakNextDir == 'D':
            self.x += 1
            
        snakDir = snakNextDir
        
    def moveNotHead(self, frontSnake):
        self.x = frontSnake.x
        self.y = frontSnake.y
        
    def update(self):
        screen.blit(self.snakeb,(self.x * snakeSize, self.y * snakeSize))
        
    
# 위치 정보 x,y(튜플)정보를 가지고 있는 리스트
snakes = []

# 시작 위치(10, 10)
for x in range(0, 3):
    snakes.append(snakebody(10-x, 10))

# 게임 루프
previous_time = time.time()  # 이전 프레임의 시간
while running:
    # 프레임 간 시간 차이 계산 (deltaTime)
    current_time = time.time()
    delta_time = current_time - previous_time
    previous_time = current_time
    moveCurrTime += delta_time

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snakDir != 'S':
                snakNextDir = 'W'
            elif event.key == pygame.K_DOWN and snakDir != 'W':
                snakNextDir = 'S'
            elif event.key == pygame.K_LEFT and snakDir != 'D':
                snakNextDir = 'A'
            elif event.key == pygame.K_RIGHT and snakDir != 'A':
                snakNextDir = 'D'
                
            #snakes[0].appendKye(snakDir)
                

    # 게임 로직 업데이트

    # 화면 그리기
    screen.fill((0, 0, 0))  # 검은색 배경
    
    for idx, s in enumerate(reversed(snakes)):
        if moveCurrTime >= moveStepTime:
            s.proc()
            if idx == len(snakes)-1:
                s.moveHead()
            else:
                s.moveNotHead(snakes[len(snakes)-1-idx-1])
                
        s.update()
        
    pygame.display.update()
        
    if moveCurrTime >= moveStepTime:		# 시간 초기화
        moveCurrTime = 0

# 게임 종료
pygame.quit()
