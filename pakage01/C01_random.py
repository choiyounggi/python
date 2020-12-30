# import : 다른 모듈을 이 소스파일에서 사용하기 위해 가져온다
# import ramdom : 랜덤 모듈을 사용하기 위해 가져옴
import random   # 뒤에 as 어쩌고를 적으면 변수 지정 가능

# random.choice(seq) : 전달한 시퀀스의 요소중 하나를 랜덤으로 선택해준다
for i in range(100):
    choice = random.choice(['얼룩말', '사자', '하마', '고양이', '늑대', '양'])
    pick = random.choice(range(30, 51, 1))

    print('선택된 동물', choice, end=', ')
    print('선택된 번호', pick)

# random.shuffle(seq) : 전달한 리스트의 순서를 무작위로 섞어준다
card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# random.shuffle(card)
# print(card)

# 맨 앞에 있는 카드를 뽑으면 확인한 뒤 카드의 맨 밑으로 넣어보세요
random.shuffle(card)
print(card[0])
card.append(card.pop(0))
print(card)

# random.randrange(a, b) : 해당 범위의 숫자중 하나를 선택해준다 (b 미만)
pick = random.randrange(1, 10) # 1 ~ 9
print('1 - 9:', pick)

# random.randrange(a) : 0부터 a미만의 숫자중 하나를 선택해준다
pick = random.randrange(10)    # 0 ~ 9
print('0 - 9:', pick)

# random.randint(a, b) : 해당 범위의 숫자중 하나를 선택해준다 (a, b포함)
pick = random.randint(1, 10)   # 1 ~ 10
print('1 - 10:', pick)

# random.sample(seq, num) : 전달한 시퀀스에서 n개의 요소를 랜덤으로 선택한다
taste = ['초코', '바닐라', '딸기', '멜론', '망고', '사과']
sample = random.sample(taste, 2)

print(sample)