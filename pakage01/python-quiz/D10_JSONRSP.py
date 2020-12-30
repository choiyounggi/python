# 전적을 json형태로 저장하는 가위바위보 게임을 만들어보세요

import random as ran
import json

record = {
    'win': 0,
    'draw': 0,
    'lose': 0
}

jsonStr = json.dumps(record)

with open('record.json', 'w') as f:
    f.write(jsonStr)

with open('record.json', 'r') as f:
    data = f.read()
    loaded = json.loads(data)

with open('record.json', 'r', encoding='utf8') as f:
    for letter in f.read():
        if letter in record:
            record[letter] += 1
print(f'당신의 전적 : {record["win"]}win {record["draw"]}draw {record["lose"]}lose')

rsp = ('가위', '바위', '보')

while True:
    jsonStr = json.dumps(record)
    com = ran.choice(rsp)
    user = input('가위, 바위, 보 중 하나를 입력하세요> ')
    if user == '종료':
        print('가위바위보 게임을 종료합니다')
        with open('record.json', 'w') as f:
            f.write(jsonStr)
        print(f'당신의 전적 : {record["win"]}win {record["draw"]}draw {record["lose"]}lose')
        break
    if user not in rsp:
        print('잘못된 입력입니다')
    else:
        if user == com:
            print('무승부 입니다!')
            with open('record.json', 'r', encoding='utf8') as f:
                    record['draw'] += 1
            print(f'현재 전적 : {record["win"]}win {record["draw"]}draw {record["lose"]}lose')
        elif user == '가위' and com == '보':
            print('당신의 승리!')
            with open('record.json', 'r', encoding='utf8') as f:
                record['win'] += 1
            print(f'현재 전적 : {record["win"]}win {record["draw"]}draw {record["lose"]}lose')
        elif user == '보' and com == '바위':
            print('당신의 승리!')
            with open('record.json', 'r', encoding='utf8') as f:
                record['win'] += 1
            print(f'현재 전적 : {record["win"]}win {record["draw"]}draw {record["lose"]}lose')
        elif user == '바위' and com == '가위':
            print('당신의 승리!')
            with open('record.json', 'r', encoding='utf8') as f:
                record['win'] += 1
            print(f'현재 전적 : {record["win"]}win {record["draw"]}draw {record["lose"]}lose')
        else:
            print('컴퓨터의 승리!')
            with open('record.json', 'r', encoding='utf8') as f:
                record['lose'] += 1
            print(f'현재 전적 : {record["win"]}win {record["draw"]}draw {record["lose"]}lose')

        print('your pick :', user)
        print('com pick :', com)
        print('승률: ', 100 / (record['win'] + record['lose']) * record['win'], '%')