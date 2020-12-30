# 사용자로부터 영어로 된 문장을 입력받고
# 해당 문장에 'a' 와 'e'가 몇 번씩 등장했는지 출력해보세요

# ※ 영어와 공백만으로 이루어진 입력이 아니라면 에러 메세지를 출력해보세요
# count1 = 0
# count2 = 0

# for sentence in list(input('문장을 입력해주세요> ')):
#     if (sentence >= 'a' and sentence <= 'z') or (sentence >= 'A' and sentence <= 'Z')\
#         and (sentence == 'a' or sentence == 'A'):
#         count1 += 1
#     if (sentence >= 'a' and sentence <= 'z') or (sentence >= 'A' and sentence <= 'Z')\
#         and (sentence == 'e' or sentence == 'E'):
#         count2 += 1
#     else:
#          print('에러) 입력이 잘못되었습니다.')
# print(f'a의 개수는 {count1}개 입니다.')
# print(f'e의 개수는 {count2}개 입니다.')

sentence = input('> ')

countA = 0
countE = 0
invalid_letter = False
for letter in sentence:
    if not ((letter >= 'a' and letter <= 'z')
            or (letter >= 'A' and letter <= 'Z')
            or letter == ''):
        invalid_letter = True   # 유효하지 않는 단어가 존재한다는 것을 표시
        # print(f'\'{letter}\'은 영어 혹은 공백이 아닙니다.')
    elif letter == 'a':
        countA += 1
    elif letter == 'e':
        countE += 1

print(f'a 등장 {countA}회 \ne 등장 {countE}회')

# bool타입 값의 활용 (flag)
if invalid_letter:
    print('※ 유효하지 않는 문자가 존재합니다.')

# list로 바꿔서 count()를 사용
print(list(sentence).count('a') + list(sentence).count('A'))

# 문자열도 시퀀스이기 때문에 count()를 사용할 수 있다
print('a의 개수: ', sentence.count('a') + sentence.count('A'))
print('e의 개수: ', sentence.count('e') + sentence.count('E'))
