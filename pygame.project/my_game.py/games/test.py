import pygame

pygame.init()

start_ticks = pygame.time.get_ticks() #시작 시간 정의


#화면 크기 설정
screen_width = 640
screen_heght = 480
screen = pygame.display.set_mode((screen_width,screen_heght))

pygame.display .set_caption("nado pang")
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드(ms)에서 초(s)로 바꾸는 것
                print(elapsed_time)

    pygame.display.update()
