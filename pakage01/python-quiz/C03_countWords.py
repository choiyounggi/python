# 1. 다음 단어들을 단어 길이별로 분류한 딕셔너리를 생성해보세요
# 2. 다음 단어들을 시작하는 알파벳으로 분류한 딕셔너리를 생성해보세요
# 3. 다음 단어들을 끝나는 알파벳으로 분류한 딕셔너리를 생성해보세요

words = ('hawk', 'giragge', 'pigeon', 'geust', 'shower', 'puzzle', 'nation', 'pilot', 'present', 'nickname', 'telephone')


# 1번 답
words_len = {}

# 단어들을 하나씩 꺼내면서 길이를 구한다 (구한 길이를 Key로 쓸 예정)
for word in words:
    length = str(len(word))

    # 해당 Key가 딕셔너리에 존재하는지 확인한다
    #   - 해당 Key가 없다면 처음 추가하는 것이므로 새로운 리스트를 생성
    #   - 해당 Key가 이미 존재한다면 그 리스트에 단어를 append
    if length not in words_len:
        words_len[length] = [word]
    else:
        words_len[length].append(word)

    print(words_len)

# 2번 답
first_word = {}

for word in words:
    first = word[0]


# 3번 답
last_word = {}