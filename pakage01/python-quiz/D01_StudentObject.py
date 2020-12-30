# 다음과 같은 학생 객체를 정의하고 테스트해보세요

# 1. 각 학생은 이름, 번호, 국어, 영어, 수학 점수가 있다

# 2. 총점을 구하는 기능

# 3. 평균을 구하는 기능

import random as ran
import datetime

class Student:
    def __init__(self, name='홍길동', num=0, kor=0, eng=0, math=0):
        self.name = name
        self.num = num
        self.kor = kor
        self.eng = eng
        self.math = math

    def getTotal(self):
        return self.kor + self.eng + self.math

    def getAvg(self):
        return self.getTotal() / 3.0

    def printStudentInfo(self):
        # strftime을 이용해 datetime객체에서 오늘 날짜만 문자열로 꺼내온다
        today = int(datetime.datetime.today().strftime('%d'))

        if today == self.num:
            print(f'{self.name}[{self.num}번] * 청소당번 *')
        else:
            print(f'{self.name}[{self.num}번]')

student_list = {
    ('홍길동', 1, 35, 35, 36),
    ('김길동', 2, 35, 35, 36),
    ('박길동', 3, 35, 35, 36),
    ('최길동', 4, 35, 35, 36),
    ('이길동', 5, 35, 35, 36),
    ('임길동', 6, 35, 35, 36),
    ('권길동', 7, 35, 35, 36),
    ('궉길동', 8, 35, 35, 36),
}

# 인스턴스를 리스트에 저장할 수도 있다
student_object_list = [
    Student('학생1', 9, 55, 56, 57),
    Student('학생2', 10, 55, 56, 57),
]

for student_tuple in student_list:
    # tuple형태의 데이터를 풀어서 __init__에 전달하여 인스턴스 생성
    student_object_list.append(Student(*student_tuple))

# 학생 객체 리스트
print(student_object_list)

for student_object in student_object_list:
    print(student_object.getAvg())

# 1. 1번부터 30번까지 랜덤 이름, 랜덤 점수를 가진 학생들의 리스트를 생성하기
test_list = []
names = ('김종민', '강호동', '은지원', '이수근')

for stuNum in range(1, 31):
    ranName = ran.choice(names)
    ranKor = ran.randint(1, 100)
    ranEng = ran.randint(1, 100)
    ranMath = ran.randint(1, 100)

    test_list.append(Student(ranName, stuNum, ranKor, ranEng, ranMath))

# 2. Student 클래스에 학생의 이름과 번호를 출력하는 기능을 추가
for student in test_list:
    student.printStudentInfo()

# 3. 오늘 날짜에 해당하는 학생이 청소당번이라고 출력해보기
