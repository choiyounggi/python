name = '홍길동'
age = 20
tel = '010-1234-1234'
height = 178.5
weight = 75
bloodType = 'O'

print('========== 출력 결과 ==========\n')
print('이름\t: %s' % (name))
print('나이\t: %d' % (age))
print('Tel\t: %s' % (tel))
print('키\t: %.1f' % (height)) # %.숫자f : 소수점 자리수 제한 (제한된 자리로 반올림)
print('몸무게\t: %.0f' % (weight))
print('혈액형\t: %c' % (bloodType))