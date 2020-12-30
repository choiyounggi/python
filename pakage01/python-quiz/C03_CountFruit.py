# 1. 랜덤 과일이 100개 저장되어 있는 리스트를 생성해보세요 (중복 허용)

# 2. 각 과일의 개수를 저장한 딕셔너리를 생성해보세요
import random as ran

fruits = ['apple', 'banana', 'kiwi', 'pineapple', 'watermelon', 'melon', 'orange', 'peach', 'cherry']
randomFruit = list()
for i in range(100):
    randomFruit.append(ran.choice(fruits))

print('1번 답:', randomFruit)

fruitCount = {}

for f in fruits:
    fruitCount[f] = randomFruit.count(f)

# for fc in len(fruits):
#     fruits[fc] = randomFruit.count(fruits[fc])

print('2번답 \n', fruitCount)

