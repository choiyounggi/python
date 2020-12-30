# while
#   - 연산 결과가 참인 동안 실행을 반복한다
#   - 연산 결과가 거짓이라면 반복을 끝낸다

import random

num = 0
while num < 20:
    print(num)
    num += 1

card = ['A', '2', '3', '4', '5', 'Joker']
random.shuffle(card)
print(card)

# Joker라는 문자열이 card리스트에 존재하는 동안 뽑는다
while 'Joker' in card:
    print('이번에 뽑은 카드:', card.pop(0))

# while문의 조건에 True를 쓰면 무한 반복을 하게 된다
# while문에도 break와 continue를 사용할 수 있다
num = 0
while True:
    print('hello!!!', num)
    num += 10000

    if num == 50000:
        break
        
# while문과 input을 활용해 프로그램을 구성할 수 있다

while True:
    user = input('가위, 바위, 보>')  # 입력을 기다리게 된다
    
    if user == '종료':
        print('while문을 빠져나가서 프로그램을 종료합니다.')
        break
        
while input('가위, 바위, 보 > ') != '종료':
    print('실행')
    
print('종료')

# 문자가 숫자가 될 수 있는지 체크해주는 함수
user = '123'
print('숫자가 될 수 있나요?', user.isdigit())

if user.isdigit():
    print('숫자가 될 수 있어서 int()를 실행합니다.')
    int(user)
else:
    print('숫자가 될 수 없는 문자입니다.')