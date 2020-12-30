# List
#   - 데이터를 여러개 저장할 수 있는 타입
#   - []를 사용한다
#   - 중복되는 데이터를 저장할 수 있다
#   - 여러가지 편리한 기능을 제공한다

# 리스트의 기본 사용
pet = ['cat', 'dog', 'pig', 'cow', 'horse', 'cobra']

print(pet)
print(type(pet))    # <class 'list'> 타입

# 리스트에는 꼭 같은 타입 데이터만 들어갈 필요는 없다
my_dog = ['몽실이', 5, 5.3, ['개껌', '방석', '산책']]
print(my_dog)

# index를 사용하면 리스트에 저장된 데이터를 하나씩 꺼낼 수 있다
#   ※ index: 리스트에서의 위치 (몇 번째 데이터인가)

print(pet)
print('pet[0]:', pet[0])
print('pet[1]:', pet[1])
print('pet[2]:', pet[2])
print('pet[3]:', pet[3])
print('pet[4]:', pet[4])
print('pet[5]:', pet[5])
# print('pet[6]', pet[6]) # 없는 index에 접근하면 에러가 발생한다 (IndexRrror)

# index를 통해 원하는 위치의 데이터를 변경할 수 있다
print(pet)
pet[4] = 'bird'
print(pet)

# 리스트를 index를 이용해 잘라서 사용할 수 있다 (slice)
print('pet[0:2]:', pet[0:2])    # pet[0:2]의 의미 - 0번 인덱스 이상 2번 인덱스 미만
print('pet[3:]\t:', pet[3:])    # pet[3:]의 의미 - 3번 인덱스 이상부터 끝까지
print('pet[:4]\t:', pet[:4])    # pet[:4]의 의미 - 처음부터 4번 인덱스 미만까지
print('원본\t\t:', pet)          # 원본이 훼손되지 않는다

# len() 함수 : 전달한 리스트의 길이를 반환한다
print('리스트 pet의 길이:', len(pet))
print('리스트 pet[2:4]의 길이:', len(pet[2:4]))

# -index : 리스트의 뒤쪽 인덱스부터 접근한다 (-1이 가장 뒤)
print('pet[-1]:', pet[-1])
print('pet[-2]:', pet[-2])
print('pet[-3]:', pet[-3])

# 다른 언어였다면 길이 -1로 접근해야 한다
# (인덱스는 0번부터 시작하기 때문에 마지막 인덱스는 항상 길이 -1이다)
print('pet[-3]:', pet[len(pet)-1])

# 비어있는 리스트 만드는 방법
listA = list()
listB = []

# list.append() : 리스트의 맨 끝에 데이터 추가하기
listA.append(10)
listA.append(20)
listB.append(99)
listB.append(5)
listB.append(13)


print(listA)
print(listB)

# listA.extend(listB) : 두 리스트를 연결하여 확장한다
listA.extend(listB)
print('listA:', listA)
print('listB:', listB)

listA.extend(listA)
print('listA + listA:', listA)

# list.insert(index, element(item)) : 원하는 위치에 요소를 추가한다
listA.insert(0, 'HI')
print(listA)

# list.pop(index) : 해당 index의 값을 꺼내면서 사용한다
#                   (인덱스를 지정하지 않으면 맨 끝의 데이터를 사용한다)
print(listA.pop(0))  # 0번의 데이터를 꺼내면서 사용
print(listA)         # 0번 데이터가 사라져있다

print(listA.pop())  # 맨 마지막 데이터 사용
print(listA)        # 확인

# list.count(element) : 해당 요소가 리스트 내에 몇 개있는지 알 수 있다
print('listA에 13은 몇개?', listA.count(13))
print('listA에 99는 몇개?', listA.count(99))

# list.sort() : 리스트를 크키순으로 정렬한다
listA.sort()    # 오름차순 정렬
print(listA)

listA.sort(reverse=True)    # 내림차순 정렬
print(listA)

# 정렬 시 정렬 기준 정해주기
fruits = ['banana', 'apple', 'kiwi', 'orange',
          'strawberry', 'watermelon', 'pineapple']

fruits.sort() # 크기 순 정렬 (문자는 사전순)
print(fruits)

# 다른 기준으로 정렬하고 싶다면 key값에 기준이 될 함수 이름을 전달해줄 수 있다
fruits.sort(key=len)
print(fruits)

# list.index(element, start) :start에서부터 원하는 값의 위치를 찾는다
listA.extend(listA)
listA.extend(listA)
print(listA)

# listA에서 13의 위치를 찾아보기
print('첫 번째 13의 위치:', listA.index(13, 0))
print('두 번째 13의 위치:', listA.index(13, 5))
print('세 번째 13의 위치:', listA.index(13, 14))
print('네 번째 13의 위치:', listA.index(13, 23))

# 더 이상 찾을 수 없으면 ValueError
# print('다섯 번째 13의 위치:', listA.index(13, 32))

# list.remove(value)
#   - 해당 요소를 삭제할 수 있다
#   - pop과는 다르게 삭제하면서 해당 값을 반환하지는 않는다
listA.remove(13)
listA.remove(99)
print(listA)