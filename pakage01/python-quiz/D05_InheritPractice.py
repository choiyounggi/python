# 클래스를 하나 정의하고 
# 해당 클래스를 상속받은 클래스를 하나 생성해보세요
# 그리고 자식 클래스에 오버라이드 메서드와
# 자식 클래스에만 있는 메서드도 추가하고 테스트 해보세요

class Car:
    def __init__(self, color='흰색', type='승용차', fuel='휘발유'):
        self.color = color
        self.type = type
        self.fuel = fuel
    def introduce(self):
        print(f'내 차는 {self.color} {self.type}야!! 연료는 {self.fuel}를 쓰지')
        
class Benz(Car):
    def __init__(self, color, type, fuel, price, company):
        super().__init__(color, type, fuel)
        self.price = price
        self.company = company
    def introduce(self):
        print(f'내 차는 {self.company}꺼야 가격은 {self.price}이고, {self.color} {self.type}야!! 연료는 {self.fuel}를 쓰지')
    def pride(self):
        print(f'{self.company}를 타고다니면 어깨가 으쓱해 무려 {self.price}짜리 차라고!!')

class BMW(Car):
    def __init__(self, color, type, fuel, price, company):
        super().__init__(color, type, fuel)
        self.price = price
        self.company = company
    def introduce(self):
        print(f'내 차는 {self.company}꺼야 가격은 {self.price}이고, {self.color} {self.type}야!! 연료는 {self.fuel}를 쓰지')
    def pride(self):
        print(f'{self.company}를 타고다니면 어깨가 으쓱해 무려 {self.price}짜리 차라고!!')

car01 = Car('흰색', '승용차', '휘발유')
car01.introduce()

car02 = Benz('빨간색', '스포츠카', '하이브리드', '7000만원', '벤츠!')
car02.introduce()
car02.pride()

car03 = BMW('검정색', 'SUV', '경유', '8500만원', 'BMW!')
car03.introduce()
car03.pride()