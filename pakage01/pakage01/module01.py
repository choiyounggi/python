import random

cmds = ['도', '개', '걸', '윳', '모']

def throwBar():
    return random.choice(cmds)

class yootGame:
    def __init__(self):
        self.player = 4
        self.price = 5000
        
# 다른 .py에서 실행한 경우에는 테스트 소스가 실행되지 않도록
# 막아줄 수 있는 방법이 있다

# module01.py를 실행한 경우에는 __name__에 들어있는 값이
# '__main__'이고, 다른 .py를 실행한 경우에는 다른 값이 들어있다

# 즉, module01.py로 실행을 한 경우에만 if문 내부의 테스트 소스가 실행되도록 한다
print('__name__의 값:', __name__)
if __name__ == '__main__':
    # 테스트를 진행 했다고 가정
    print(cmds[3])
    print(cmds[4])