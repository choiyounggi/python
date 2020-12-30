# 사과를 10개씩 담을 수 있는 바구니가 있다

# 사과의 개수를 입력하면 필요한 바구니의 개수를 출력해주는 
# 프로그램을 만들어보세요

apple_num = int(input('사과의 개수를 입력해주세요> '))

if apple_num <= 0:
    print('사과의 개수가 잘못되었습니다.')
elif apple_num % 10 == 0:
    print(f'필요한 바구니의 개수는 {apple_num / 10}개 입니다.')
else:
    print(f'필요한 바구니의 개수는 {(apple_num // 10) + 1}개 입니다.')