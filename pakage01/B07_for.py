# for
#   - 시퀀스의 모든 내용을 하나씩 꺼내면서 반복한다
#   - 해당 시퀀스의 마지막 요소까지 모두 꺼낸 후 종료된다
#   - 하나씩 꺼낸 모든 값에 for문 내부의 명령을 적용한다

# 모든 시퀀스들을 for문에 활용할 수 있다
# for문 범위는 들여쓰기 레벨로 설정할 수 있다
for animal in ['cat', 'dog', 'mouse', 'lion']:
    print(animal)

for num in (1, 2, 3, 4, 9):
    print('-' * 20)
    print(' ' * 8, num)
print('-' * 20)

for num in {3, 4, 5, 6, 7}:
    print(f'set: {num}, ', end='')
print() # 빈 print()는 줄만 바꾼다 (end의 기본값 \n)

for ch in 'Hello python!':
    print(ch)

for i in range(100, 0, -2):
    print(i)

# 반복문을 이용해서 총합 구하기

# 1. 총합을 저장할 변수를 0으로 만들어 둔다 (sum, total)
start = int(input('시작값 > '))
end = int(input('끝값 > '))

sum = 0

# 2. 반복하면서 만들어둔 변수에 값을 계속 누적시킨다
for i in range(start, end + 1):
    sum += i

print('총합:', sum)