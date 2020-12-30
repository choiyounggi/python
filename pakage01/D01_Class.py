# 객체지향 프로그래밍 (OOP: Object Oriented Programming)
#   - 세상에 존재하는 모든 개념을 변수와 함수로 표현하려는 방식

# 객체 (object)
#   - 세상에 존재하는 모든 개념
#   - ex: 강의실, 학생, 버튼, 유닛, 턴 ....

# 사과
#   - 변수(상태) : 색깔, 크기, 당도, 데미지
#   - 함수(기능) : 먹는다(크기 -), 썩는다(색깔 변화, 당도 변화),
#                던진다(데미지) ...

# 클래스 (Class)
#   - 객체를 프로그래밍 언어로 표현한 것
#   - 클래스는 해당 객체의 설계도
#   - 클래스를 정의한 시점에서는 실체가 없다
#   - 클래스를 통해 생성한 실체를 '인스턴스(instance)'라고 부른다

# 인스턴스 (instance)
#   - 객체를 통해 만들어진 실체
#   - 똑같은 설계도로 만들어졌지만 각자 다른 값을 가질 수 있다
#     ex: 사과는 초록색일 수도 있고, 빨간색일 수도 있다
#   - 클래스 내부에서 self는 인스턴스 자기 자신을 가리킨다

class Apple:
    # 클래스 내부의 __init__() 함수
    #   - 인스턴스를 생성할 때 가장 먼저 호출되는 함수
    def __init__(self, color='기본 색', size='기본 크기', damage='기본 데미지', sweet='기본 당도'):
        self.color = color
        self.size = size
        self.damage = damage
        self.sweet = sweet

    # 클래스 내부에 정의하는 함수는 해당 클래스가 가진 기능(method)이된다
    def throwApple(self, target):
        print(f'{target}가 사과를 맞고 {self.damage}만큼의 데미지를 입었습니다.')

# 클래스를 통해 실체(인스턴스)를 생성하기
#   - 클래스 이름을 함수처럼 사용하여 인스턴스를 생성한다
#   - 생성할 때 클래스 내부의 __init__가 요구하는 파라미터를 전달해 줘야 한다
apple01 = Apple(color='red', size=10, damage=5, sweet=3.5)
apple02 = Apple('초록색', 9, 6, 4.3)
apple03 = Apple()   # 아무것도 전달하지 않은 인스턴스는 기본 값을 지닌다

# 생성된 클래스의 값을 확인하기
print('사과1의 색깔:', apple01.color)
print('사과1의 크기:', apple01.size)
print('사과1의 데미지:', apple01.damage)
print('사과1의 당도:', apple01.sweet)

print('사과2의 색깔:', apple02.color)
print('사과2의 크기:', apple02.size)
print('사과2의 데미지:', apple02.damage)
print('사과2의 당도:', apple02.sweet)

print('사과3의 색깔:', apple03.color)

apple01.throwApple('민수')
apple02.throwApple('민수')

# 클래스를 통해 생성된 인스턴스에 .을 찍으면
# 해당 인스턴스의 변수와 메서드를 이용할 수 있다 