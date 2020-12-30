# 딕셔너리
#   - key/Value 방식으로 데이터를 관리하는 파이썬의 자료구조
#   - 탐색이 빠르고 사용이 편리하다
#   - 같은 이름의 키는 하나만 존재할 수 있다

# key:Value 형태로 데이터를 저장한다
p1 = {
    'name': '홍길동',
    'age': '20',
    'gender': 'male',
}

# 값을 꺼낼때는 Key를 이용한다
print('p1의 name:', p1['name'])
print('p1의 age:', p1['age'])
print('p1의 gender:', p1['gender'])
print('p1의 타입:', type(p1))

# 존재하지 않는 키로 값을 꺼내면 KeyError가 발생한다
# print(p1['hobby'])

# 존재하지 않는 키에 값을 넣으면 새로운 Key:Value가 추가된다
p1['hobby'] = 'soccer'
print(p1['hobby'])
print(p1)

# 딕셔너리를 반복문과 함께 활용할 수 있다 (Key를 하나씩 꺼내면서 반복한다)

for key in p1:
    print(f'{key}:{p1[key]}')

# dict.keys() : 모든 키들을 반환한다
print(p1.keys())

# dict.values() : 모든 값들을 반환한다
print(p1.values())

# dict.get(key) : 해당 Key로 값을 하나 꺼낸다
print(p1.get('hobby'))
print(p1['hobby'])

# dict.items() : 딕셔너리 내부의 모든 것을 (키, 값) 형태의 튜플로 반환한다
print(p1.items())

for k, v in p1.items():
    print(k, v)

# 딕셔너리의 데이터 삭제
del p1['hobby']
print(p1)

# in 연산자와 딕셔너리를 사용하면 해당 값을 가진 key가 있는지 알 수 있다
print('name이라는 Key가 p1에 있나요?', 'name' in p1)
print('hobby라는 Key가 p1에 있나요?', 'hobby' in p1)

# dict.clear() : 딕셔너리의 모든 내용을 지운다
p1.clear()
print(p1)