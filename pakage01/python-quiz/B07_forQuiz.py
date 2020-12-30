# 정수를 하나 입력받고

# 1. 1부터 입력받은 수 까지의 합을 구해보세요.

# 2. 1부터 입력받은 수 중에서 5의 배수만 출력해보세요.

# 3. 1부터 입력받은 수 중 7의 배수의 합을 출력해보세요.

# 4. 1부터 입력받은 수 중 3의 배수가 모두 몇 개 있는지 출력해보세요

num = int(input('정수를 입력해주세요> '))
sum1 = 0
sum2 = 0

print('1번 답')
if num < 0:
    print('정수가 아닙니다.')
else:
    for a in range(1, num + 1):
        sum1 += a
    print(f'총 합은 {sum1}입니다.')
print()

print('2번 답')
if num < 0:
    print('정수가 아닙니다.')
elif num > 5:
    a = list(range(5, num + 1, 5))
    print(f'1에서 입력하신 수 까지의 5의 배수는 {a}입니다.')
else:
    print('1에서 입력하신 수 사이에 5의 배수가 존재하지 않습니다.')
print()

print('3번 답')
if num < 0:
    print('정수가 아닙니다.')
elif num > 7:
    for a in range(7, num + 1, 7):
        sum2 += a
    print(f'1에서 입력하신 수 까지의 7의 배수들의 합은 {sum2}입니다.')
else:
    print('1에서 입력하신 수 사이에 7의 배수가 존재하지 않습니다.')
print()

print('4번 답')
if num < 0:
    print('정수가 아닙니다.')
elif num > 3:
    print(f'1에서 입력하신 수 중 3의 배수의 갯수는 {num // 3}개 입니다.')
else:
    print('1에서 입력하신 수 사이에 3의 배수가 존재하지 않습니다.')



