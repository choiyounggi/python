# Escape 문자
#   - 앞에 \가 붙어서 특수한 기능을 하는 문자들
#   - \n, \t, \\, \", \', \b

# \n : 줄바꿈의 기능을 하는 특수 문자
print('안녕하세요! 반\n갑습니다.')

# \t : Tab키의 기능을 하는 특수 문자
print('안녕하세요! 반\t갑습니다.')

# \b : BackSpace키의 기능을 하는 특수 문자
print('안녕하세요! 반\b갑습니다.')

# \\ : 그냥 역슬래시를 출력하고 싶은 경우에 사용
print('C:\\Program Files\\JetBrains\\Pycharm')

# \". \' : 그냥 작은따옴표(큰따옴표)를 출력하고 싶은 경우에 사용
print("'용기를 내야 해' 사람들이 말헀습니다.") # 바깥과 안의 따옴표를 다른게 쓰면 상관 x
print('"용기를 내야 해" 사람들이 말했습니다.') # 바깥과 안의 따옴표를 다른게 쓰면 상관 x

print("용기를 내서 이렇게 말했습니다. \"나는 못해요\"")
print('용기를 내서 이렇게 말했습니다. \'나는 못해요\'')

######################################################################
print('hello') # 작은 따옴표 (큰 따옴표) 사이에 넣는 값은 문자로 인식한다
print(123)     # 작은 따옴표 (큰 따옴표) 바깥에 사용하는 숫자는 숫자로 인식한다
print('123')   # 작은 따옴표 (큰 따옴표) 내부에 사용하는 숫자는 문자로 인식한다

print("123 + 123은?", 123 + 123)
# print("123 + 123은?", "123" + 123)   # 문자와 숫자를 더해서 에러가 발생했다