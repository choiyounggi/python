# 비교 연산
#   - 두 값의 크기를 비교하는 연산
#   - 비교 연산의 결과는 True 혹은 Flase이다 (bool 타입)

a, b = 20, 3

print('a가 b보다 더 큰가요?', a > b)
print('a가 b보다 더 작나요?', a < b)
print('a가 b보다 더 크거나 같나요?', a >= b)
print('a가 b보다 더 작거나 같나요?', a <= b)

print('a와 b가 같은 값인가요?', a == b) # 두 값이 같으면 True
print('a와 b가 다른 값인가요?', a != b) # 두 값이 다르면 True

# 문자도 비교가 가능하다 (사전상으로 늦게 등장하는 단어가 더 크다)
# ※ 문자들은 실제로 각자의 코드값을 가지고 있다.
#   만약 a가 97이라면 b가 98, c는 99가 된다.
#   컴퓨터가 단어의 사전순을 아는것이 아니라 실제 코드값을 사전순으로 설정해놓은 것이다.
word1, word2, word3 = 'airplane', 'subway', 'apple'

print(word1 > word2)
print(word1 < word2)
print(word1 < word3)

word1, word2 = 'apple', 'apple'
print(word1 == word2)
print(word1 != word2)

# 논리 연산
#   - True/False로 연산을 한다
#   - and, or, not이 있다

# and : 두 값이 모두 True일때만 True
print('True and True:', True and True)
print('True and false:', True and False)
print('False and True:', False and True)
print('False and False:', False and False)

# 비교연산의 결과는 bool타입이기 때문에 논리연산과 비교연산을 함께 이용하는 경우가 많다
num = 30
print(num < 20 and num % 5 == 0)

# or : 둘 값중 하나만 True여도 True
print('True or True:', True or True)
print('True or false:', True or False)
print('False or True:', False or True)
print('False or False:', False or False)

# 나이가 7세 미만이거나 65세 이상이라면 할인 대상임을 표현하고 싶을 때
age = 35
discount_target = age < 7 or age >= 65
print(f'{age}살은 할인대상 {discount_target}입니다.')

# not : 참이면 거짓, 거짓이면 참
print(not True)
print(not False)

print(not age < 7)