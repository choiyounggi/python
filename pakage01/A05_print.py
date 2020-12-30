# 기본
print('hello')
print(123 + 456)

# ,와 함께 사용
name = '홍길동'
print('name:', name)
print('age:', 20)

# print가 자동으로 줄을 바꾸지 않게 하기
# print의 end값을 다른 값으로 설정하면 줄이 바뀌지 않게 된다
# (end의 기본값은 \n이다, 기본값이란? 아무것도 설정하지 않았을 떄의 값)
print('안녕하세요', end=', ')
print('반갑습니다')

# 서식을 이용하는 방법
#   %s : 문자열 (문자 여러개)
#   %c : 문자 (문자 단 하나)
#   %d : 정수
#   %f : 실수 (소수)
#   %x : 정수를 16진수로
#   %o : 정수를 8진수로
date = '오늘'
weather = '맑음'
year = 2020
month = 9
day = 25
print('%s의 날씨. %s. %d년 %d월 %d일' % (date, weather, year, month, day))

# 서식문자 옵션
print('%d' % 123)       # 그냥 출력
print('%10d' % 123)     # 10칸 확보하고 123출력
print('%20d' % 123)     # 20칸 확보하고 123출력

print('%20s%20s%20s' % ('NAME', 'AGE', 'BLOOD'))
print('-------------------------------------------------------------')
print('%20s%20d%20s' % ('John Doe', 23, "AB"))
print('%20s%20d%20s' % ('Harry potter', 17, "O"))
print('%20s%20d%20s' % ('Hermione', 17, "B"))

print('%-10d:' % 123)    # 10칸 확보하고 왼쪽 정렬해서 출력
print('%-20d:' % 123)    # 20칸 확보하고 왼쪽 정렬해서 출력

print('%010d' % 123)    # 10칸 확보하고 빈칸을 0으로 채움
print('%020d' % 123)    # 20칸 확보하고 빈칸을 0으로 채움

print('%+d' % 123)  # 양수일떄도 부호를 표시해준다 (원래는 음수일때만 표시)

print('%30.5f' % 123.123456789)     # 30칸 확보하고 소수점 자릿수는 5자리 제한

# % formatting
#   - % formatting은 print에만 사용되는것이 아니라 변수에 저장할 수도 있다

you = '김만식'
me = '홍길동'
my_age = 25
intro = '안녕하세요, %s씨. 제 이름은 %s입니다. 나이는 %d살 입니다.' %(you, me, my_age)

print(intro)

# f string
intro = f'안녕하세요, {you}씨. 제 이름은 {me}입니다. 나이는 {my_age}살 입니다.'
print(intro)





