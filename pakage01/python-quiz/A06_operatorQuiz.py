# 당신은 놀이공원을 가기 위해 11개의 지하철 역을 지나왔다.
# 출발 역에서 도착역까지 37분이 걸렸다면
# 한 역을 지나는데 걸리는 시간은 얼마인가?
# (소수점 2자리 까지 출력)

subway_station_num = 11
time = 37

print('한 역을 지나는데 걸리는 시간: %.2f' % (time / subway_station_num) + '분')




# f-string에서 서식문자 옵션을 적용하는 방법
print(f'{time / subway_station_num:.3}분')

# round(val, ) 함수
#   - 값 하나만 넣으면 해당 값을 정수로 반올림
#   - 값을 두개 넣으면 두번째 넣은 값으로 반올림
print(f'{subway_station_num}개의 역을 지나는데 {time}분이 걸렸다면')