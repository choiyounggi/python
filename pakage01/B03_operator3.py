# 대입연산자
a = 2   # 왼쪽의 변수에 오른쪽 값을 넣는다
a += 2  # a = a + 2
print(a)
a -= 10 # a = a - 10
print(a)
a *= 5  # a = a * 5
print(a)
a //= 3  # a = a / 3
print(a)

# in 연산자
#   - 해당 값이 시퀀스 내부에 포함되어 있는지 여부를 반환한다
#   ※ 시퀀스 : 문자열, 리스트처럼 나열할 수 있는 성질을 가진 것들
msg = 'Hello python class!'

print('py라는 단어가 msg에 포함되어 있나요?', 'py' in msg)
print('hello라는 단어가 msg에 포함되어 있나요?', 'hello' in msg)
print('hello' in 'hello, world!')

snacks = ['감자칩', '스윙칩', '포테토칩', '허니버터칩', '프링글스', '도리토스']
print('초코송이' in snacks)
print('허니버터칩' in snacks)
print('포카칩' in ['칸쵸', '칙촉', '누네띠네', '마이쮸'])