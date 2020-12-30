# 우리가 변수를 사용해야 하는 이유
#   1. 값을 한번에 변경할 수 있다 => 2번 이상 사용할 값은 변수를 사용하는 것이 좋다
#   2. 값에 의미를 부여할 수 있다 => 변수의 이름을 잘 짓는것은 매우 중요하다

apple_num = 20      # 사과의 개수
apple_price = 599   # 사과의 개당 가격
apple_calorie = 98  # 사과의 개당 칼로리

print('사과의 개수: ', apple_num, '\b개')
print('개당 가격: ', apple_price, '\b원')
print('개당 칼로리: ', apple_calorie, '\bkcal')
print('사과의 총 가격: ', '￦', apple_num * apple_price)
print('사과의 총 칼로리: ', apple_num * apple_calorie, '\bkcal')

# 권장되는 변수의 작명 규칙
#   - 지키지 않아도 에러는 발생하지 않는 규칙들
#   - 개발자들 간의 약속

#   (1) 두 단어 이상을 이어붙인 변수명을 사용할 때는 _를 사용하자 (snake_case)
#       ex: minsu_score, personal_score, best_score, max_size ...

#   (2) 두 단어 이상을 이어붙인 변수명을 사용할 때는 대문자를 사용하자 (camelCase)
#       ex: minsuScore, maxSize, currValue, nextValue ...

#   (3) 변수의 첫 글자는 소문자를 사용하는 것이 좋다

#   (4) 값이 변하지 않을 변수(상수)는 이름을 모두 대문자로 짓는다
#       ex: APPLE_CALORIE, PI, MAX_SCORE ...

#   (5) 변수의 값이 어떤 값인지 추측할 수 있는 이름을 사용하자

# 필수적인 변수의 작명 규칙
#   - 지키지 않으면 문법적인 에러가 발생하는 규칙들

#   (1) 변수명 첫 글자는 숫자가 될 수 없다
#       ex: 1st, 2nd, 4pple ...

#   (2) 변수 사이에는 공백을 사용할 수 없다

#   (3) 특수문자는 _와 $만 사용할 수 있다

#   (4) 이미 사용하고 있는 키워드(예약어)는 변수명으로 사용할 수 없다
#       ex: True, False, for, class, if, elif, continue, break, ...