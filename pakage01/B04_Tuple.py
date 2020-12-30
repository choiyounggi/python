# Tuple
#   - 리스트와 비슷하지만 ()를 사용한다
#   - 튜플에는 요소를 추가/수정/삭제 할 수 없다
#   - 읽기 전용 리스트라고 할 수 있다

tuple1 = (10, 20, 30)

print(tuple1)
print(10 in tuple1)
print(tuple1[1])
print(tuple1[1:])

# x, y, z = (10, 20, 30)
x, y, z = tuple1
print(x, y, z)

x, y, z = [30, 35, 50]  # list도 가능함
print(x, y, z)

something = 30, 40, 50, 60  # 괄호를 생략하고 나열하면 튜플이 된다
print(type(something))

# 리스트는 튜플이 될 수 있고 튜플도 리스트가 될 수 있다
#   ※ 시퀀스끼리는 서로간의 변환이 자유롭다
listA = list(something) # list()함수에 시퀀스를 전달하면 리스트로 변환해준다
listB = list('Hello!! My name is sausage.')

print(listA)
print(listB)

tupleA = tuple(listA)
tupleB = tuple(listB)

print(tupleA)
print(tupleB)

# str() 함수를 통해 문자열이 되기는 하지만 (), []들이 함께 문자열이 된다 (쓸모없다)
strA = str(tupleA)
strB = str(tupleB)
strC = str(9999)

print(strA)
print(strB)
print(strC)

# 추가/수정/삭제 불가능
# tupleA[0] = 'abc'
# tupleA.append()