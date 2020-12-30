# 가위바위보 프로그램을 만들어보세요

# 1. 프로그램을 시작하면 컴퓨터가 가위/바위/보 중 하나를 랜덤으로 선택

# 2. 사용자가 가위/바위/보 중 하나를 입력하면 승/무/패를 출력
import random as ran

# user = input('가위/바위/보 중 하나를 입력해주세요> ')
# rsp = ['가위', '바위', '보']
# random.shuffle(rsp)
#
# print('컴퓨터:', rsp[0])
# print('사용자:', user)
#
# for i in user:
#     if user == rsp[0]:
#         print('비겼습니다.')
#     elif user == '가위' and rsp[0] == '바위':
#         print('졌습니다.')
#     elif user == '바위' and rsp[0] == '보':
#         print('졌습니다.')
#     elif user == '보' and rsp[0] == '가위':
#         print('졌습니다.')
#     elif user == '가위' and rsp[0] == '보':
#         print('이겼습니다.')
#     elif user == '바위' and rsp[0] == '가위':
#         print('이겼습니다.')
#     elif user == '보' and rsp[0] == '바위':
#         print('이겼습니다.')
#     else:
#         print('잘못된 입력입니다.')

rsp = ('가위', '바위', '보')

com = ran.choice(rsp)
user = input('가위, 바위, 보 중 하나를 입력하세요> ')

# 잘못된 입력을 꼭 걸러주자
if user not in rsp:
    print('잘못된 입력입니다')
else:
    if user == com:
        print('무승부 입니다!')
    elif user == '가위' and com == '보':
        print('당신의 승리!')
    elif user == '보' and com == '바위':
        print('당신의 승리!')
    elif user == '바위' and com == '가위':
        print('당신의 승리!')
    else:
        print('컴퓨터의 승리!')

    print('your pick :', user)
    print('com pick :', com)