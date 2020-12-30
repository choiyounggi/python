# Class 영역
#   - 같은 클래스로 만들어진 모든 인스턴스가 공유하는 영역

import  random as ran

class Apple:
    # 클래스 영역에 선언하는 값은 모든 인스턴스에서 같은 값을 가지게 된다
    # 인스턴스 개수와 관계없이 하나만 생성되게 된다
    color_list = ['빨간색', '초록색', '벌레벅은색']

    # 클래스 영역에 선안한 값들은 클래스 이름에 .을 찍고 사용할 수 있게 된다

    def __init__(self, size):
        # self에 저장되는 값은 사과가 100개 생성된다면 100개 생성된다
        # 모든 사과에서 같은 값을 지녀야하는 color_list가 100개 있을 필요는 없다
        # self.color_list = ('빨간색', '초록색', '벌레먹은색')
        self.size = size
        self.color = ran.choice(Apple.color_list)

apple_basket = []

for i in range(100):
    apple_basket.append(Apple(10))

# 클래스 영역의 값은 모든 인스턴스에서 바라보고 있기 때문에
# 하나만 수정해도 모든 인스턴스에서 값이 변하는 효과가 있다
Apple.color_list[2] = '주황색'

print(apple_basket[0].color_list)
print(apple_basket[1].color_list)

# 각자의 인스턴스 영역이 필요하지 않은 변수를
# 클래스 영역으로 옮기면 메모리 공간이 많이 절약된다
