# import turtle
# t = turtle.Turtle()
# t.speed(0)
# for i in range(99999):
#     t.forward(50)
#     t.right(4)
#     t.left(90)
# import turtle
# t = turtle.Turtle()
# t.speed(0)
# line = 3
# while True:
#     line1 = 360 / line
    

#     for i in range(line):
#         t.forward(50)
#         t.right(line1)
  
        
#     t_pos = t.pos()
#     t.penup()
#     t.goto(0,t_pos[1]+10)
#     t.pendown()
#     line += 1









































# a = 0

# import turtle
# t = turtle.Turtle()
# t.speed(0.5)
# line = 3
# while True:
#     line1 = 360 / line
    

#     for i in range(line):
#         t.forward(50)
#         t.right(line1)
#     line += 1
#     t.penup()

#     t.pendown()
#     t.setheading(0)
#     a += 10

# import time
# import turtle

# t = turtle.Turtle()
# t.speed(0)

# def quit_program():
#     turtle.bye()  # 터틀 그래픽 종료
# def left():
#     t.setheading(180)
#     t.forward(4)
# def up():
#     t.setheading(90)
#     t.forward(4)
# def down():
#     t.setheading(-90)
#     t.forward(4)
# def right():
#     t.setheading(0)
#     t.forward(4)
# def clear():
#     t.clear()
#     t.penup()
#     t.goto(0,0)
#     t.pendown()

# def key():
#     global time1
#     global time2
#     time2 = time1
#     time1 = time.time()
#     print(time2)
#     turtle.write(time1,align="center")
# # # 키보드 이벤트 핸들러 등록
# # turtle.onkeypress(quit_program, 'q')

# turtle.onkeypress(key,"a")

# turtle.onkeypress(right,"d")

# turtle.onkeypress(up,"w")

# turtle.onkeypress(down,"s")

# turtle.onkeypress(clear,"space")

# # 터틀 그래픽 시작
# turtle.listen()
# turtle.mainloop()


# time1 = -1


# time2 = 0

# def key():
#     global time1
#     global time2
#     t.undo()
#     time2 = time1
#     time1 = time.time()
#     print(time2)
#     turtle.write(time1,align="center")
# turtle.listen()

    


# turtle.onkeypress(key,"space")


# if time2 == time1:
#     time3 = round(time1,0)
#     t.penup()
#     t.goto(0,-time3)
#     t.pendown()
#     t.circle(time3)

    

# turtle.listen()
# turtle.mainloop()















































# # import turtle

# # t = turtle.Turtle()


# # while True:
# #     t.shape("blank")
# #     t.forward(5)

# import turtle

# # 터틀 객체 생성
# t = turtle.Turtle()

# # 화살표 모양 없애기
# t.shape("blank")

# # 이후에 그리기 명령어 사용
# t.forward(100)
# t.right(90)
# t.forward(100)

# # 터틀 창 유지
# turtle.done()

# import turtle

# # 터틀 객체 생성 후 화살표 모양 없애기
# t = turtle.Turtle()
# t.shape("blank")
# window = turtle.Screen()
# window.bgcolor(135, 206, 250)  # 하늘색
# # 이후에 그리기 명령어 사용
# t.forward(100)
# t.right(90)
# t.forward(100)

# # 터틀 창 유지
# turtle.done()


# import turtle

# # 터틀 창 생성
# window = turtle.Screen()

# # 배경색 설정
# window.bgcolor("pink")  # 하늘색

# # 터틀 창 유지
# turtle.done()

# import socket

# surver_port =
# import socket

# def is_port_in_use(port):
#     try:
#         # 소켓 생성
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             # 포트와 연결 시도
#             s.bind(('localhost', port))
#     except socket.error:
#         # 포트가 사용 중인 경우
#         return True

#     # 포트가 사용 중이지 않은 경우
#     return False

# # 특정 포트 번호가 사용 중인지 확인
# port = 57396
# if is_port_in_use(port):
#     print(f"포트 {port}는 사용 중입니다.")
# else:
#     print(f"포트 {port}는 사용 가능합니다.")
# import socket

# def run_client():
#     host = 'localhost'  
#     port = 8000  

#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((host, port))  

#     while True:
        
#         message = input('메시지 입력:')

#         if message.lower() == 'q':
#             break

#         client_socket.sendall(message.encode('utf-8'))

#         response = client_socket.recv(1024).decode('utf-8')
#         print('서버 응답:', response)

#     client_socket.close()

# if __name__ == '__main__':
#     run_client()

l = []
for i in range(5):
    l.append(i)

print(l)
l[2].pos