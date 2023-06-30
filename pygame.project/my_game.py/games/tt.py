count = 1  # 변수 카운트를 위한 초기값

while True:
    user_input = input("변수 이름을 입력하세요 (종료하려면 'q'를 입력): ")

    if user_input == 'q':
        break

    # 변수 동적 생성
    variable_name = user_input + str(count)
    exec(f"{variable_name} = '{user_input}'")

    # 생성된 변수 사용
    print(eval(variable_name))

    count += 1