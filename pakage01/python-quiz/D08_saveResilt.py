# 가위바위보 게임을 컴퓨터와 진행하도록 만들고
# 승패를 파일에 기록해보세요 (10개마다 \n으로 개행)

# 기록 예시 > 승승패패패승패승패승승패패패...
import random as ran
rsp = ('가위', '바위', '보')
c = 0

while True:
    com = ran.choice(rsp)
    user = input('가위, 바위, 보 중 하나를 입력하세요> ')
    if user not in rsp:
        print('잘못된 입력입니다')
    else:
        if user == com:
            print('무승부 입니다!')
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('무\n')
        elif user == '가위' and com == '보':
            print('당신의 승리!')
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승')
        elif user == '보' and com == '바위':
            print('당신의 승리!')
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승')
        elif user == '바위' and com == '가위':
            print('당신의 승리!')
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승')
        else:
            print('컴퓨터의 승리!')
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('패\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('패')

        print('your pick :', user)
        print('com pick :', com)