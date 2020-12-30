# 클래스 상속
#   - 이미 존재하는 클래스를 그대로 물려받은 뒤 개조해서 사용할 수 있다
#   - 기본 틀이되는 간단한 공통 부분을 부모 클래스로 구현한 뒤
#     각자 상속받아 세부적인 구현을 진행한다
#   - 라이브러리 제작자들이 기본틀을 만들어두고,
#     사용자는 상속받아 해당 객체를 이용한다

class Person:
    job = '무직'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'안녕! 내 이름은 {self.name}이야. 나이는 {self.age}살이야.')

# class 자식클래스(부모클래스)로 클래스를 선언하면 상속이 된다
# 자식클래스는 부모클래스의 모든 기능을 포함하고 있다

#   자식클래스 : sub class, child class
#   부모클래스 : super class, parent class
class Programmer(Person):
    # 오버라이드
    #   - 부모에게 이미 존재하는 자원(변수, 메서드)을 마음대로 수정하여 사용하는 것
    #   - 같은 이름으로 자식 클래스에서 다시 정의하여 현재 클래스의 상황에 맞게
    #     고쳐서 사용할 수 있다
    job = '프로그래머'
    
    # 상속받은 클래스는 __init__에서 부모 클래스의 __init__를 먼저 호출해야 한다
    # super() : 현재 인스턴스의 부모 부분에 접근할 수 있다
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    # 메서드 오버라이드 : 같은 이름으로 다른 기능을 적용할 수 있다
    def introduce(self):
        print(f'저는 프로그래머 {self.name}입니다. 연봉은 {self.salary}받습니다.')

    # 부모에게 존재하지 않는 메서드도 마음대로 추가하여 사용할 수 있다
    def program(self, order):
        print(f'{self.name}씨는 외주를 받아 {order}을 만들기로 했습니다.')

person01 = Person('길동', 10)
person02 = Programmer('민수', 20, 3000)

print('person01의 직업:', person01.job)
print('person02의 직업:', person02.job)

person01.introduce()
person02.introduce()

person01.program('오목')
person02.program('퍼즐게임')