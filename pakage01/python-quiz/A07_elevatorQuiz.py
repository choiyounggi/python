# 600kg 제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 무게를 실수로
# 입력받아 현재 엘리베이터에 더 적재할 수 있는 무게를 구하시오

# 첫 번째 물건의 무게를 입력하시오> 64.27
# 두 번째 물건의 무게를 입력하시오> 75.25
# 현재 엘리베이터에 허용 무게는 460.48kg 입니다.

weight_limit = 600
first_weight = input('첫 번째 물건의 무게를 입력하시오> ')
second_weight = input('두 번째 물건의 무게를 입력하시오> ')
allow_weight = 600 - (float(first_weight) + float(second_weight))

if (allow_weight >= 0):
    print('현재 엘리베이터에 허용 무게는 %.2fkg 입니다.' % allow_weight)
else:
    print('허용 무게를 초과했습니다. 물건의 무게를 다시 입력해주세요')