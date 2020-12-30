# 알맞은 비교 연산을 만들어보세요
#   1. age가 14이상이고 20미만일 때 True
#   2. ch가 'x' 혹은 'X' 일 때 True
#   3. ch가 공백 또는 탭이 아닐 때 True
#   4. ch가 알파벳일 때 True (대/소문자 모두 포함)
#   5. year가 400으로 나누어 떨어지거나
#      또는 4로 나누어 떨어지고 100으로 나누어 떨어지지 않을 때 True
#   6. latecome이 False일 때 True
age = 4
ch = 'a'
year = 2020
latecome = True


print('1번')
print(age >= 14 and age < 20)

print('2번')
print(ch == 'x' or ch == 'X')

print('3번')
print(ch != ' ' or ch != '\t')

print('4번')
print((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'))

print('5번')
print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

print('6번')
print(not latecome)