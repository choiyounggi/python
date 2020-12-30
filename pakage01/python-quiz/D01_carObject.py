# 1. 자동차 객체는 타입과 번호판이 있다

# 2. 타입에는 '장애인, 유아동승, 긴급, 해당없음'이 있다

# 3. 자동차 객체에는 오늘 내 차가 주차장에 입장할 수 있는지 여부를
#    True/False로 반환하는 메서드가 있다

# 4. 랜덤으로 차량 10대를 생성하고 3번의 메서드를 테스트 해보세요

# datetime 모듈에서 date만 가져오기
from datetime import date

import random as ran


# t = ['월', '화', '수', '목', '금']
# 
# r = datetime.datetime.today().weekday()

# class car:
#     def __init__(self, num, carType):
#         self.num = num
#         self.type = carType
#
#     def Enter_access(self):
#         num = str(self.num)
#         numList = list(num)
#
#         if self.type == '해당없음':
#             if t[r] == '월' and int(numList[2]) == 1 and int(numList[3]) == 6:
#                 print('월요일에는 끝번호 16 차량은 출입이 제한됩니다')
#             if t[r] == '화' and int(numList[2]) == 2 and int(numList[3]) == 7:
#                 print('화요일에는 끝번호 27 차량은 출입이 제한됩니다')
#             if t[r] == '수' and int(numList[2]) == 3 and int(numList[3]) == 8:
#                 print('수요일에는 끝번호 38 차량은 출입이 제한됩니다')
#             if t[r] == '목' and int(numList[2]) == 4 and int(numList[3]) == 9:
#                 print('목요일에는 끝번호 49 차량은 출입이 제한됩니다')
#             if t[r] == '금' and int(numList[2]) == 5 and int(numList[3]) == 0:
#                 print('금요일에는 끝번호 50 차량은 출입이 제한됩니다')
#         else:
#             print('출입이 가능합니다')
#
# types = ('장애인', '유아동승', '긴급', '해당없음')
#
# carList = []
#
# for ranCar in range(1, 11):
#     num1 = str(ran.randint(0, 9))
#     num2 = str(ran.randint(0, 9))
#     num3 = str(ran.randint(0, 9))
#     num4 = str(ran.randint(0, 9))
#     numList = [num1, num2, num3, num4]
#     ranType = ran.choice(types)
#
#     num = int(''.join(numList))
#
#     carList.append(car(num, ranType))

CAR_TYPES = ['장애인', '유아동승', '긴급', '해당없음']
CAR_LIMITS = {
    'Mon': (1, 6),
    'Tue': (2, 7),
    'Wed': (3, 8),
    'Thr': (4, 9),
    'Fri': (5, 0)
}

class Car:
    def __init__(self, car_type, num_plate):
        self.car_type = car_type
        self.num_plate = num_plate
    def park_able(self):
        weekday = date.today().strftime('%a')
        print('요일:', weekday)

        if self.car_type != '해당없음':
            return self.create_park_msg(True, '주차 가능한 타입의 차량입니다.') # True
        
        # 해당없음 타입의 차량들만 날짜에 따른 주차여부를 체크한다
        # last_num = f'{self.num_plate:04}'[-1]
        last_num = self.num_plate % 10

        if weekday in CAR_LIMITS:
            # 차량 번호 체크
            if last_num in CAR_LIMITS[weekday]:
                return self.create_park_msg(False, '오늘 출입제한인 번호입니다.') # False
            else:
                return self.create_park_msg(True, '오늘은 주차 가능한 번호입니다.') # True
        else:
            return self.create_park_msg(True, '오늘은 주말입니다.') # True
    def create_park_msg(self, park_able, reason):
        return f'[{self.num_plate:04}/{self.car_type}] - '\
               f'{park_able} : {reason}'

cars = []
for i in range(10):
    ranPlate = ran.randint(0, 9999)
    cars.append(Car(ran.choice(CAR_TYPES), ranPlate))

for car in cars:
    print(car.park_able())