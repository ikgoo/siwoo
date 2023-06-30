# import pygame

# # Pygame 초기화
# pygame.init()

# # 화면 크기 설정
# screen_width = 640
# screen_height = 480
# screen = pygame.display.set_mode((screen_width, screen_height))

# # 색 설정 (RGB)
# black = (0, 0, 0)
# white = (255, 255, 255)

# # 네모 그리기
# rect_width = 50
# rect_height = 50
# rect_x = 100
# rect_y = 100
# pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height))

# # 화면 업데이트
# pygame.display.update()

# # 게임 루프
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         screen.fill((255,255,255))

# # Pygame 종료
# pygame.quit
text = "이시우/천재/ㅋ"
splitted = text.rsplit('/', 1)

if len(splitted) > 1:
    result = splitted[-1]
else:
    result = text

print(result)  # 출력: ㅋ