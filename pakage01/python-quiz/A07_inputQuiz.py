# 올해 년도와 태어난 년도를 구하여 나이를 계산하는 프로그램을 코딩하시오

# 올해의 년도를 4자리로 입력하세요?
# 당신이 태어난 년도를 4자리로 입력하세요?
# 당신의 나이는 ?? 살 입니다.

this_year = input('올해의 년도를 4자리로 입력하세요> ')
born_year = input('당신이 태어난 년도를 4자리로 입력하세요> ')
age = int(this_year) - int(born_year) + 1

print(f'당신의 나이는 {age}살 입니다.')





