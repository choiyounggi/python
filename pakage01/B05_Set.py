# Set
#   - 집합을 구현한 자료구조
#   - 아이템(요소)의 중복을 허용하지 않는다
#   - {}를 사용한다

# 빈 set()생성
setA = set()

# append() 대신 add()가 있다
setA.add(10)
setA.add(10)
setA.add(10)    # 중복된 값은 추가되지 않는다
setA.add(20)
setA.add(30)

print(setA)

# set을 이용하면 다른 시퀀스의 중복 데이터를 쉽게 제거할 수 있다
msg = 'asdasdasdasdasdasdasda'
existing_alphabet = set(msg)
print(existing_alphabet)

# Set에는 중복을 저장할 수 없다
setB = {1, 2, 2, 3, 3, 4, 5, 6, 7}
print(setB)

# union() : 합집합을 구해서 새로운 합집합 Set을 반환한다 (원본에 영향을 미치지 않는다)
unionSet = setA.union(setB)
print(unionSet)

# list의 extend는 원본을 변형시키지만
# set의 union은 원본을 그대로 유지한 채 새로운 set을 반환한다
listA = [10, 20, 30]
listB = [10, 20, 30]

listA.extend(listB)
print(setA)

# intersection() : 교집합을 구한다
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 7, 9}

interSet = setA.intersection(setB)
print(interSet)

# difference() : 차집합을 구한다
diffSet1 = setA.difference(setB) # A - B
print(diffSet1)

diffSet2 = setB.difference(setA) # B - A
print(diffSet2)

# Set은 index가 존재하지 않는다 (순서가 없다, 정렬이 불가능하다)
print(setA)
# print(setA[B])    # 불가능

# list를 변환해도 순서가 뒤죽박죽이다
print(set(['z', 'i', 'b', 'r', 'a']))

# set.remove(value) : 값을 지울 수 있다
setA.remove(5)
print(setA)

# set.update(seq) : 시퀀스를 Set에 추가할 수 있다
# (add는 1개 추가, update는 여러개 추가)
setA.update('Republic of korea')
setA.update(['car', 'bmw', 'benz', 'audi'])
setA.update((10.3, 10.5, 33.33))

print(setA)

