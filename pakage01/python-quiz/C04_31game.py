# while문을 이용해 31게임을 만들어보세요

# 1. 컴퓨터와 사람이 번갈아가면서 숫자를 선택한다

# 2. 컴퓨터는 랜덤으로 숫자를 선택한다

# 3. 선책할 수 있는 숫자는 1, 2, 3이다

# 4. 31을 부르는 사람이 패배한다
a = 31
import random as ran

while a > 0:
    user_pick = input('숫자를 입력해주세요> ')
    if (user_pick.isdigit()) and (int(user_pick) > 0 and int(user_pick) < 4):
        a -= int(user_pick)
        if a <= 0:
            print('컴퓨터의 승리입니다.')
            break
        print(f'{int(user_pick)}을 선택하셨습니다. 남은 숫자는 {a}개 입니다.')
        com_pick = ran.randint(1, 3)
        a -= com_pick
        if a <= 0:
            print('사용자의 승리입니다.')
            break
        print(f'컴퓨터는 {com_pick}을 선택했습니다. 남은 숫자는 {a}개 입니다.')

    else:
        print('1 ~ 3의 숫자 중 하나를 입력해주셔야합니다. 다시 입력해주세요')



