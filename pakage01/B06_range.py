# range
#   - 특정 범위의 숫자를 만들어주는 함수
#   - range(시작, 끝, 증가폭)
#   - 리스트, 튜플 등으로 변환할 수 있다

# range() 함수에 숫자를 한개만 넣으면 0부터 넣은 숫자까지의 range를 생성한다
# (시작값은 0이되고 끝값이 설정된다, 증가폭은 1)
print(range(10))        # range(0, 10)을 이용해 리스트 생성
print(list(range(10)))  # 0 ~ 9 까지의 숫자가 생성되었다
print(tuple(range(20)))

# range로 생성하는 숫자 범위는 시작값부터 끝값 -1이다 (index와 함께 사용하기 좋다)

# range() 함수에 숫자를 두개 넣으면 시작, 끝 값이 설정된다. 증가폭은 1이다
a = range(20, 25)
print(set(a))

# range() 함수에 숫자를 세 개 넣으면 시작, 끝, 증가폭을 모두 설정한다
rangeA = range(5, 99, 3)
rangeB = range(100, 0, -1)  # 증가폭에 -값을 사용할 수도 있다

print(list(rangeA))
print(tuple(rangeB))