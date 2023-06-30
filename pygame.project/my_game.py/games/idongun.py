# import random
# running = 0 #돌고 있냐
# while running == 0:                      # "*"
#     test1 = random.randint(1,9)          #b = print(str(b) + "*")
#     test2 = random.randint(1,9)          #b = "3"
                            
#     print("구구단을 외자")
#     answer = input(str(test1) +"*" + str(test2) + "=")

#     if answer == str(test1 * test2):
#         print("정답")
#     else:
#         print("응 너 졌어 ㅋ")
#         running = 1


# print(2<1)
# sow = 2<1 #여기 변수에 2>1 = True가 있잖아 그럼 sow를 쓸때 True 라고 인식하는거야 근데 print()를 쓰면 밑에 출력하는 거야 근데 그걸 변수에 넣으면 sow는 숫자나 문자만 받아 근데 print()는 숫자나 문자가 아닌 파이썬 문자야 그래서 오류가 나 
# print(sow + 1>0)

from turtle import Turtle
from turtle import Screen
import time



import random

def left():
    if snakes[0].heading()  != 0:
        snakes[0].setheading(180)
        
def down():
    if snakes[0].heading()  != 90:
        snakes[0].setheading(270)

def right():
    if snakes[0].heading()  != 180:
        snakes[0].setheading(0)

def up():
    if snakes[0].heading()  != 270:
        snakes[0].setheading(90)



def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape('square')
    snake_body.color('orangered')
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x,rand_y
def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f'점수 : {score}', font = ('배찌체', 15, 'bold'))

def game_over():
         score_pen.goto(0,0)
         score_pen.pd()
         score_pen.write('Game Over', False, 'center', ('배찌체', 30, 'bold'))

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('khaki')
screen.title('Snake Game')
screen.tracer(0)

start_pos = [(0,0), (-20,0), (-40,0)]
snakes = []
score = 0

for pos in start_pos:
    create_snake(pos)

food = Turtle()
food.shape('circle')
food.color('snow')
food.up()
food.speed(0)
food.goto(rand_pos())

score_pen = Turtle()
score_pen.ht()
score_pen.pu()
score_pen.goto(-270, 250)
score_pen.write(f'점수 : {score}', font = ('배찌체', 15, 'bold'))

screen.listen()
screen.onkeypress(up, 'Up')
screen.onkeypress(down, 'Down')
screen.onkeypress(right, 'Right')
screen.onkeypress(left, 'Left')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())
    snakes[0].forward(10)

    if snakes[0].distance(food) < 15:   
        score_update()
        food.goto(rand_pos())                                                                           
        create_snake(snakes[-1].pos())

    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 \
        or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
         game_on = False
         game_over()

    for body in snakes[1:]:
        if snakes[0].distance(body) < 10:
            game_on = False
            game_over()
