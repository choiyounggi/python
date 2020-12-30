# static method
#   - 클래스 영역과 인스턴스 영역 모두 사용하지 않고
#     매개변수만으로 동작하는 메서드
#   - 객체지향 요소가 빠져있는 클래스 활용법이다
class Calculator:
    @staticmethod
    def plus(a, b):
        return a + b
    @staticmethod
    def minus(a, b):
        return a - b

class Emoji:
    @staticmethod
    def rabbit():
        return ' /)/)\n(  ..)\n(  >☆'

print(Emoji.rabbit())