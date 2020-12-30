# 웹 서버에 요청을 보내서 응답을 받아올 수 있는 모듈
# 별도의 설치가 필요하다

# python에서 외부의 모듈을 다운받을떄는 pip라는 프로그램을 사용한다

import requests

# 웹 서버로 요청을 보낸다는 것은
# 웹 브라우저를 켜서 주소창에 주소를 입력하는 것과 같다
response = requests.get('https://comic.naver.com/index.nhn')

print(response.status_code)
print(response.encoding)

htmlCode = response.text

# print('랭킹1위의 인덱스:', htmlCode.find('<li class="rank01'))

ranking = []

for i in range(1, 6):
    found_index = htmlCode.find(f'<li class="rank0{i}')
    # print(f'랭킹{i}위의 인덱스:', found_index)
    close_tag_index = htmlCode.find('</li>', found_index)
    # print(f'랭킹{i}위의 닫는 태그 인덱스:', close_tag_index)
    ranking.append(htmlCode[found_index:close_tag_index])

myHtmlCode = '<ol>'

for r in ranking:
    myHtmlCode += r
myHtmlCode += '</ol>'

print(myHtmlCode)

# 만들어진 코드로 파일 생성
with open('result/webtoon.html', 'w', encoding='utf8') as f:
    f.write(myHtmlCode)

