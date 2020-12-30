# input() 함수
#   - input()함수를 사용하면 사용자의 입력을 기다린다
#   - 사용자가 값을 입력하면 그 값을 str타입으로 받아온다
#   - input()함수에 전달한 문자열은 안내문구 역할을 한다
station = input('역의 개수를 입력해주세요> ')
time = 37

# 입력받은 값은 str로 들어오기 떄문에 int()로 변환하여 계산해야 한다
print('한 역 당 {time/int(station):.3}분 걸렸습니다.')