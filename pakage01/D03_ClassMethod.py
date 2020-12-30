# 인스턴스 메서드
#   - 인스턴스 변수(self)들을 이용해 기능을 구현하는 메서드

# 클래스 메서드
#   - 클래스 변수(cls)들을 활용해 기능을 구현하는 메서드
#   - 메서드 바로 위에 @classmethod를 추가해서 표시한다

# 문제 1. 승객의 화물을 bus_trunk 딕셔너리에 추가하는 메서드를 만들어보세요
#        승객의 좌석번호가 Key값이 되고, value는 승객의 화물 리스트입니다.
#        bus_trunk에 물건을 실었다면 승객의 cargo리스트는 텅 비어야 합니다.

class Passenger:
    bus_trunk = {}

    def __init__(self, name, seat, cargo):
        self.name = name
        self.seat = seat
        self.cargo = cargo

    # 일반적인 인스턴스 메서드
    def information(self):
        # 인스턴스 메서드에서 클래스 영역의 자원을 활용할 수 있다
        return f'승객명 - {self.name} / 좌석 - {self.seat} / ' \
               f'트렁크 - {Passenger.bus_trunk}'

    # 사용하면 승객이 버스 트렁크에 물건을 싣는 메서드
    def load(self):
        Passenger.addToBusTrunk(self.seat, self.cargo)
        self.cargo = list()

    @classmethod
    def addToBusTrunk(cls, seat, cargo):
        # 클래스 영역에서는 인스턴스 영역의 자원을 활용할 수 없다
        cls.bus_trunk[seat] = cargo



pass01 = Passenger('개똥이', 'A1', ['치약', '칫솔', '물', '화장품'])
pass01.load()
print(Passenger.bus_trunk)