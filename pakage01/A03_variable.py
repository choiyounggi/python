# 변수란?
#   - 값을 담아둘 수 있는 공간
#   - 담아둔 값을 나중에 꺼내서 자유롭게 사용할 수 있다
#   - 한번 값을 담아두면 변경할 때 까지 계속 값이 유지된다

# 프로그래밍 언어의 = (대입연산)
#   - 여태까지 알고있는 =의 의미 : 왼쪽 값과 오른쪽 값이 같다
#   - 프로그래밍 언어에서 =의 의미 : 왼쪽의 변수에 오른쪽의 값을 넣어라 (10 = x 는 불가능)
x = 10

print(x)
print(x + x)
print('x에 들어있는 값 : ', x)

# 변수에 들어갈 수 있는 값들
x = 10          # 숫자 (정수: int)
print(x, type(x))
x = 123.123     # 숫자 (실수: float)
print(x, type(x))
x = 'hello'     # 문자 (str)
print(x, type(x))
x = True        # 참/거짓 bool
print(x, type(x))
x = False       # 참/거짓 bool
print(x, type(x))

# type() 함수
#   - ()에 전달한 값의 타입을 알려준다
result = type('Hi')
print('검사 결과', result)

# 변수에 저장된 값을 이용해 계산도 할 수 있다
x = 10
y = 30

print('x + y: ', x + y)
print('x - y: ', x - y)
print('x * y: ', x * y)
print('x / y: ', x / y)

# 한 줄에 변수를 여러개 선언할 수도 있다
x, y, z = 10, 11, 12

print(x)
print(y)
print(z)

# 두 변수의 값을 바꿔치기 할 수도 있다
x, y = 3, 33
x , y = y, x

print(x)
print(y)

# 변수를 더 이상 사용하고 싶지 않을때 지울 수 있다
del x
del y

# print(x)
# print(y)

for a in range(2, 10):
    for b in range(1, 10):
        print(a,'단:', a, 'x', b, '=', a * b)



