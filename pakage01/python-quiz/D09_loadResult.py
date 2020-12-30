# 가위바위보 게임을 실행하면 처음에 파일에서 데이터를 읽어오고
# 읽어온 데이터로 전적을 출력해보세요

# 그 뒤 게임이 진행되고 진행결과도 계속 저장되도록 만들어보세요

import random as ran

record = {
    '승': 0,
    '무': 0,
    '패': 0
}

with open('rsp.sav', 'r', encoding='utf8') as f:
    for letter in f.read():
        if letter in record:
            record[letter] += 1
print(f'당신의 전적 : {record["승"]}승 {record["무"]}무 {record["패"]}패')


rsp = ('가위', '바위', '보')

c = 0
w = 0
r = 0
m = 0

while True:
    com = ran.choice(rsp)
    user = input('가위, 바위, 보 중 하나를 입력하세요> ')
    if user == '종료':
        print('가위바위보 게임을 종료합니다')
        print('현재까지의 전적')
        print(f'{w + r + m}전: 승리 {w}번 / 패배 {r}번 / 무승부 {m}번')
        print(f'승률: {(100 / (w + r) * w):.2f}%')
        break
    if user not in rsp:
        print('잘못된 입력입니다')
    else:
        if user == com:
            print('무승부 입니다!')
            m += 1
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('무\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('무')
        elif user == '가위' and com == '보':
            print('당신의 승리!')
            w += 1
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승')
        elif user == '보' and com == '바위':
            print('당신의 승리!')
            w += 1
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승')
        elif user == '바위' and com == '가위':
            print('당신의 승리!')
            w += 1
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('승')
        else:
            print('컴퓨터의 승리!')
            r += 1
            c += 1
            if c % 10 == 0:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('패\n')
            else:
                with open('../result/rspResult.txt', 'a', encoding='utf8') as f:
                    f.write('패')

        print('your pick :', user)
        print('com pick :', com)
        print('전적')
        with open('../result/rspResult.txt', 'r', encoding='utf8') as f:
            for line in f.readlines():
                print(line, end='')
        print('')
        print(f'{w + r + m}전: 승리 {w}번 / 패배 {r}번 / 무승부 {m}번')
        print(f'승률: {(100 / (w + r) * w):.0f}%')