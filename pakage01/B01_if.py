# if문
#   - if문 옆의 조건이 True라면 if문에 속한 명령을 실행한다
#   - 조건이 False라면 if문에 속한 명령을 무시한다
#   - if문의 범위는 들여쓰기로 구분한다.

# elif문
#   - 반드시 if문 다음에 연속으로 사용해야 한다
#   - 위의 if문 혹은 elif문이 거짓이라면 if문처럼 조건을 체크한다
#   - elif는 여러개 사용할 수 있다

# else문
#   - 반드시 if문 또는 elif문 다음에 사용해야 한다
#   - 위의 조건들이 모두 아니라면 else에 속한 명령을 무조건 실행한다

# Crtl + / : 블록 지정된 곳을 주석처리
# animal = input('> ')
#
#   if animal == 'rabbit':
#   print(' /)/)')
#   print('(  ..)')
#   print('(  >☆')

num = 33

# 위의 조건이 아닐때만 elif가 실행된다
# 위의 조건에서 True가 발생하여 실행되는 if문이 있다면 elif는 실행되지 않는다
if num > 10000:
    print('num은 10000보다 큰 숫자입니다.')
elif num > 1000:
    print('num은 1000보다 큰 숫자입니다.')
elif num > 100:
    print('num은 100보다 큰 숫자입니다.')
elif num > 50:
    print('num은 50보다 큰 숫자입니다.')
else:
    print('위의 조건이 모두 아닙니다.')