# 택시 요금 144m당 3000원
# 할증 20% (할증 시간 - 새벽 0시 ~ 4시)일 때

# 시간과 거리를 입력하면 택시 요금을 계산해주는 프로그램을 만들어보세요

hour = input('시간을 입력해주세요(24시간 기준)> ')
minute = input('분을 입력해주세요> ')
distance = input('거리를 입력해주세요(m단위)> ')

fee = int(distance) * (3000 / 144)
over_fee = fee * 1.2

if (int(minute) < 0 or int(minute) > 59) and (int(hour) < 0 or int(hour) > 23):
    print('존재하지 않는 시간입니다')
elif int(hour) < 4:
    print(f'금액은 {over_fee} 입니다.')
elif int(hour) < 23 or int(hour) >= 4:
    print(f'금액은 {fee}입니다.')
