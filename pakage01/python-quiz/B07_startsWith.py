# 다음 words 단어들 중 a로 시작하는 단어가 모두 몇개인지 세어보세요
# hint. 문자열도 인덱스를 사용할 수 있음

words = 'apple', 'banana', ' orange', 'kiwi', 'among', 'us', 'account'


count = 0
for word in words:
    if word[0] == 'a':
        count += 1

print('a가 들어간 단어의 개수:', count)

# 문자열도 인덱스 사용이 가능하다
print('kiwi'[0])
print('kiwi'[2:4])

# 튜플에 들어있는 문자열의 첫번째 글자에 한번에 접근하기
# count = 0
# for a in range(0, 6):
#     if words[0][0] == 'a':
#         count += 1
#         print(count)

# for문으로 데이터를 꺼낼 때의 2가지 스타일

# 1. 요소를 순서대로 하나씩 꺼내는 스타일
for word in words:
    
    print(word)

# 2. range()를 index 목록을 생성하여 그 번호를 통해 접근하는 스타일
for index in range(len(words)):
    print(words[index])