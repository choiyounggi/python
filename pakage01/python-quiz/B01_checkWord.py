# 두 단어를 입력받고
# 두 단어중 사전상으로 먼저 등장하는 단어가 무엇인지
# 알려주는 프로그램을 작성해보세요

word = input('첫번째 단어를 입력해주세요> ')
word2 = input('두번째 단어를 입력해주세요> ')

if word > word2:
    print(f'{word}가 사전상으로 먼저 등장하는 단어입니다.')
elif word2 > word:
    print(f'{word2}가 사전상으로 먼저 등장하는 단어입니다.')
else:
    print('두 단어는 같은 단어입니다.')