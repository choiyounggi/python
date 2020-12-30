# 사용자로부터 문장을 입력받은 후
# 한번도 등장하지 않은 알파벳을 모두 출력해보세요

# sentence = set(input('문자를 입력해주세요> '))
#
# from string import ascii_letters
#
# alpha = set(ascii_letters)
#
# diff_alpha = alpha.difference(sentence)
#
# print(diff_alpha)

text = input('> ')

alphabet_list = list('abcdefghijklmnopqrstuvwxyz')

for letter in text:
    # 알파벳 목록에 letter가 아직 남아있다면 리스트에서 letter를 지워라
    if letter in alphabet_list:
        alphabet_list.remove(letter)

print(alphabet_list)