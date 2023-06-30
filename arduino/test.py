import serial
import time

# 시리얼 포트와 속도 설정
serial_port = 'COM3'  # 사용하는 포트에 맞게 변경해주세요
baud_rate = 9600

# 아두이노와의 시리얼 통신을 위한 객체 생성
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# 아두이노로 데이터 보내기
def send_data(data):
    ser.write(data.encode())
    print(f"Sent: {data}")

# 아두이노에서 데이터 받기
def receive_data():
    data = ser.readline().decode().strip()
    if data:
        print(f"Received: {data}")

# 메인 루프
while True:
    # 사용자로부터 입력 받기
    user_input = input("Enter a message (or 'q' to quit): ")
    
    if user_input == 'q':
        break
    
    # 아두이노로 데이터 보내기
    send_data(user_input)
    
    # 아두이노에서 데이터 받기
    receive_data()

# 시리얼 포트 닫기
ser.close()
