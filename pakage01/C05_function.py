# 함수
#   - 미리 만들어둔 기능을 나중에 불러다 쓰는 것
#   - 정의한 시점에서는 실행되지 않고 호출해야 실행된다

# 함수를 정의 (실행되지 않음)
def printRabbit():
    print(' /)/)')
    print('(( ..)')
    print('(  >♡')

# 함수를 호출
printRabbit()

# 매개변수 (argument)
#   - 매개변수를 정의해 놓으면 함수를 호출할 때 필요한 값을 전달할 수 있다

# ex: 두 숫자를 전달받으면 그 합을 출력해주는 함수
def hap(a, b):
    print(a + b)

# 매개변수가 있는 함수를 호출할 때는 값을 전달해야 한다
hap(3, 10)
hap(1, 9)

# ex: 년도를 전달받으면 그 해가 윤년인지 알려주는 함수를
def bonusYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f'{year}년은 윤년입니다.')
    else:
        print(f'{year}년은 윤년이 아닙니다.')
bonusYear(2020)
bonusYear(2021)

# ex: 단어를 전달받으면 n번째 단어만 출력해주는 함수
def getLetter(word, n):
    if n > len(word) or n < 0:
        print(f'{word}의 {n}번째 글자는 없습니다.')
    else:
        print(f'{word}의 {n}번째 글자는 \'{word[n - 1]}\'입니다')

getLetter('banana', 4)
getLetter('apple', 2)
getLetter('apple', 9)

# 연습문제 > 두 단어를 매개변수로 전달받으면 사전상으로 먼저 등장하는 단어가
#           어떤 단어인지 출력해주는 함수를 정의해보세요

def printSmallWord(first_word, second_word):
    if first_word < second_word:
        print(f'{first_word}이/가 사전상 먼저 등장하는 단어입니다.')
    else:
        print(f'{second_word}이/가 사전상 먼저 등장하는 단어입니다.')

printSmallWord('1', 'koka')

# 함수의 반환 (return)
#   - 함수는 호출한 곳에 함수의 실행 결과를 반환해 줄 수 있다
#   - return을 만나는 즉시 함수가 종료된다
#   - return으로 돌려주는 값이 해당 함수를 호출한 곳에 반환된다

# ex: 두 단어를 전달하면 더 작은 단어를 반환해주는 함수
def getSmallWord(wordA, wordB):
    return wordA if wordA < wordB else wordB

# 반환이 있는 함수는 값을 받아서 사용할 수 있다
# 반환이 없는 함수는 None을 반환한다
smaller = getSmallWord('horse', 'south')
print('getSmallWord의 결과:', smaller)

smaller = printSmallWord('horse', 'south')
print('printSmallWord의 결과:', smaller)




