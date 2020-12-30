# 연산자 (operator)
#   - 계산 할 때 쓰는 것

# 산술 연산
a = 3
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # 나누기 (정확)
print(a // b)   # 나누기 (몫만 나옴)
print(a % b)    # 나머지
print(a ** b)   # 제곱

# 계산할때 사칙연산 우선순위가 반영된다. (곱하기, 나누기가 먼저 계산된다)
# 괄호도 사용할 수 있다
c = 5
print(2 + 10 * 3)
print((2 + 10) * 3)

# 정수와 실수를 연산하면 결과가 실수가 된다
print(3 + 3.5)
print(3 + 4.0)

# 정수에 .0을 붙이면 실수
print(type(4))
print(type(4.0))

# 문자끼리 더하면 두 문자를 이어붙인다
msg = 'Hello, ' + 'everyone!'
print(msg)

print('123' + '456')    # 문자 + 문자 : 이어붙임
print(123 + 456)        # 숫자 + 숫자 : 계산함

# 값의 타입을 변환하기
#   - 문자와 숫자를 더해야 하는 상황에서는 계산할지 이어붙일지를 결정해줘야 한다
print(str(123) + '456') # str(123)함수를 이용해 123을 문자로 변환
print(123 + int('456')) # int('456')함수를 이용해 456을 숫자로 변환

print(float(123))
print(bool(123))    # 숫자를 bool로 변환하면 0을 제외한 나머지는 모두 True가 된다
print(bool(0))      # 숫자를 bool로 변환하면 0은 Flase가 된다

