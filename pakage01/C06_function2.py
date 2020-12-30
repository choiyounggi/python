import random as ran

def function01(a, b, c):
    print(f'a:{a}, b:{b}, c:{c}')

# 함수의 다양한 사용법

# 1. 기본 (위치를 이용해 인수 전달)
function01(1, 2, 3)

# 2. 언패킹 (시퀀스를 풀면서 인수 전달, positional argumentss)
#   - sample로 뽑은 3개의 리스트를 인자로 풀어서 전달
listA = [3, 6, 9, 12, 15, 18, 21, 24, 27]
function01(*ran.sample(listA, 3))

# 3. 매개변수를 직접 선택하며 전달 (keyword argument)
#   - 위치를 무시하고 매개변수를 직접 선택할 수 있다
#   - 키워드 인수는 위치 인자 다음에 등장해야 한다 (등장 순서)
#   - 하나의 매개변수에 여러 값이 입력되면 안된다
function01(c=10, a=20, b=30)
# function01(c=10, 3, 5)  # 키워드 인자가 먼저 등장함
# function01(1, 2, a=20)  # a에 여러값이 들어감
function01(1, 2, c=10)

# print()의 키워드 매개변수
#   - end (default: \n)
#   - sep (default: 공백)
print(1, 2, 3, 4, 5, end='\tby 최영기\n', sep='/')

# 4. 딕셔너리를 언패킹하면 전달
#   - 매개변수명과 인자값을 담은 딕셔너리를 풀면서 전달할 수 있다
#   - 앞에 *을 두 개 붙인다
myDict = {
    'c': 55,
    'a': 66,
    'b': 77
}
function01(**myDict)

# 가변 인수
#   - 매개 변수의 개수가 정해지지 않은 함수를 정의할 수 있다
#   - 가변 인수와 매개 변수 이름은 원하는대로 지어도 되지만, 
#     관례적으로 args라고 짓는 편이다
#   - 전달하는 값들은 하나의 튜플 타입으로 전달된다
#   - 고정 인수와 함께 사용할때는 반드시 고정 인수가 먼저 등장해야 한다
def hap(name, age, *args):
    for args in args:
        print('args:', args)

hap(10, 20, 30, 40, 50, 60, 70, 80)
hap(*[10, 20, 30, 40])

# 키워드 가변 인수 (kworgs)
#   - 키워드 매개 변수를 가변적으로 받을 수 있다
#   - 전달하는 값들은 딕셔너리로 전달된다
#   - 다른 이름을 사용해도 되지만 관례적으로 kworgs를 사용한다

def printKeyValue(**kworgs):
    for key in kworgs:
        print(f'{key}={kworgs[key]}')

printKeyValue(size=10, width=100, height=200, value='red', style='color')