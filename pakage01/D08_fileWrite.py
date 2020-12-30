# print() - 콘솔에 출력
# 콘솔 대신 파일에 출력하면 저장한 데이터가 계속 유지된다

# 파일 객체 생성하기
#   with open(경로, 모드, 인코딩) as 변수:
#   'w' : 쓰기 모드
#   'r' : 읽기 모드
#   'wb' : 바이너리 쓰기 모드
#   'rb' : 바이너리 읽기 모드

# 문자가 깨지는 경우 encoding='utf8'을 추가
with open('result/test01.txt', 'a', encoding='utf8') as f:
    f.write('hello! test01!!\n')
    f.write('hello! test01!!\n')
    f.write('hello! test01!!\n')
    f.write(' /)/)\n')
    f.write('(  ..)\n')
    f.write('(  >☆\n')