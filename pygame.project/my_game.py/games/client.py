# import socket

# def run_client():
#     host = 'localhost'  # 서버 주소
#     port = 57396  # 포트 번호

   
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((host, port))  # 서버에 연결
#     name = input("이름을 입력해주세요")
#     while name == "" or None:
#         name = input("이름을 입력해주세요")
#     client_socket.sendall(name.encode('utf-8'))
#     while True:
#         # 사용자로부터 메시지 입력
#         message = input('메시지를 입력하세요 (종료하려면 q 또는 Q를 입력): ')

#         if message.lower() == 'q':
#             break

#         # 메시지를 서버로 전송
#         client_socket.sendall(message.encode('utf-8'))

#         # 서버로부터 응답 수신
#         response = client_socket.recv(1024).decode('utf-8')
#         print('서버 응답:', response)

#     # 소켓 종료
#     client_socket.close()

# if __name__ == '__main__':
#     run_client()








