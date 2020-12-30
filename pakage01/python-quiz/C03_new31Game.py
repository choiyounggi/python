import random as ran
valid_numbers = [1, 2, 3]
game_number = 0
user_turn = True

while True:

    # user_turn이 True일 때 사용자로부터 입력을 받는다
    if user_turn:
        number = input('당신 > ')

        if number.isdigit():
            number = int(number)
        else:
            print('숫자가 될 수 없는 것을 입력하셨습니다.')
            continue  # 밑의 코드를 모두 무시하고 다시 반복문 처음으로 돌아간다

        if number not in valid_numbers:
            print('1, 2, 3 중에 선택하셔야 합니다.')
            continue
    else:
        number = ran.choice(valid_numbers)
        print(f'컴퓨터 > {number}')  # 컴퓨터가 선택한 숫자는 안보이므로 출력해줌

    game_number += number
    print(f'현재 숫자 : {game_number}')

    if game_number >= 31:
        # 삼항연산자
        #   - A if 조건 else B
        #   - 가운데 조건이 참이면 A를 선택한다
        #   - 가운데 조건이 거짓이면 B를 선택한다

        # winner = '컴퓨터' if user_turn else '당신'
        if user_turn:
                winner = '컴퓨터'
        else:
                winner = '당신'

        print(f'{winner}의 승리')

    user_turn = not user_turn  # user_turn을 반전