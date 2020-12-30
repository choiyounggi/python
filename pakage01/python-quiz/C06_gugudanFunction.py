# 다음과 같이 사용할 수 있는 구구단 함수를 만들어 보세요

def printGugudan(dan, gop):
    for gugudan in range(1, gop + 1):
        print(f'{dan}단: {dan} x {gugudan} = {dan * gugudan}')

    
printGugudan(dan=8, gop=19) # 8단, x1 ~ x19까지 출력이 되야함

# 다음과 같이 사용할 수 있는 함수를 만들어보세요
def moneyFormat(price):
    price = str(price)
    price_length = len(price)

    # 100000 : 7
    # 0123456 : 8


def printPurchase(**kwargs):
    print('name' + ' ' * 15 + 'price')
    print('--------' * 3)
    total = 0
    for product in kwargs:
        price = kwargs[product]
        total += price

        # ,를 붙이는 작업을 추가
        # 가격을 전달해주면 알맞은 곳에 ,를 추가하는 함수를 작성하고 price를 전달

        print(f'{product:15}|{price:8}')
    print('--------' * 3)
    print(f'total{total:10}$')

cart = {
    'snack': 5000,
    'drink': 8000,
    'toy': 25000,
    'dogGum': 19000,
    'catLeap': 19900
}
printPurchase(**cart)

# 카트의 내용물들이 변하더라도 하나의 함수로 실행 가능해야 함

