# 다른 파일의 변수, 함수, 클래스 가져다 사용해보기
import pakage01

# pakage01에서 작성한 소스를
# import를 통해 다른곳에서 사용할 수 있다
print(pakage01.cmds)
print(pakage01.throwBar())

newGame = pakage01.yootGame()

print(newGame.player)
print(newGame.price)