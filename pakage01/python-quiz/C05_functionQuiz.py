# 다음의 함수를 정의해보세요

# 1. 전달한 숫자가 3의 배수이면 True 아니라면 False를 반환하는 함수

# 2. 전달한 숫자가 짝수라면 '짝수입니다.'를 홀수라면 '홀수입니다.'를 반환하는 함수

# 3. 사과의 개수와 바구니의 크기를 전달하면 필요한 바구니의 개수를 반환하는 함수

# 4. 문장을 전달받으면 모든 문자가 각각 몇 번 등장했는지 저장한 딕셔널를 반환하는 함수

# 1번 문제 답
def threeTimesCheck(num):
    if num % 3 == 0:
        return True
    else:
        return False
threeTimesCheck(6)

def check3(num):
    return num % 3 == 0

# ※ 리턴 값이 True/False인 함수를 만들고 싶을 때는 비교연산 자체를 리턴한다

# 2번 문제 답
def twin_or_solo(num):
    if num % 2 == 0:
        return '짝수입니다.'
    else:
        return '홀수입니다.'
twin_or_solo(34)

def checkEvenOdd(num):
    return '짝수입니다.' if num % 2 == 0 else '홀수입니다'



# 3번 문제 답
def appleBasket(appleNum, basketSize):
    if not appleNum == basketSize:
        return f'{(appleNum // basketSize) + 1}개의 바구니가 필요합니다.'
    else:
        return f'{(appleNum // basketSize)}개의 바구니가 필요합니다.'
appleBasket(6, 5)

def getBasketNum(appleNum, basketSize):
    if appleNum % basketSize > 0:
        return appleNum // basketSize + 1
    else:
        return appleNum // basketSize

# 4번 문제 답
# 문장을 전달받으면 모든 문자가 각각 몇 번 등장했는지 저장한 딕셔널를 반환하는 함수
def charCount(word):
    words = list(word)
    word = {}
    for i in words:
        word[i] = words.count(i)
    return word
charCount('banana')

def countLetter(text):
    count_dict = dict()
    for letter in text:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
        return count_dict

# 5번 문제 답
# 5. 여러 단어로 이루어진 리스트를 전달하면 
#   길이가 5글자인 단어들만으로 튜플을 생성하여 반환하는 함수
listA = ['banana', 'apple', '12345', '55555']
def manyWord(list):
    newlist = []
    for i in list:
        if len(i) == 5:
            newlist.append(i)
            t = tuple(newlist)

    return t

result = manyWord(listA)

print(result)

def wordFilter(word_list):
    result = list()
    for word in word_list:
        if len(word) == 5:
            result.append(word)
    return tuple(result)

# 6. 여러 숫자로 이루어진 리스트를 전달하면 짝수인 값만 남기는 함수
numbers = ['123', '999', '7070', '8800']
def leaveJjack(numList):
    result = list()
    for jjack in numbers:
        if int(jjack) % 2 == 0:
            result.append(jjack)
    return result

a = leaveJjack(numbers)
print(a)