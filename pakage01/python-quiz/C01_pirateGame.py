# 통아저씨 게임을 만들어보세요
# 1. 10개의 칼을 넣을 수 있는 구멍이 있다
# 2. 그 중 3개는 찌르면 아저씨가 발사된다
# 3. 나머지 7개는 찔러도 아무런 반응이 없다
# 4. 찌른곳을 또 찌를수는 없다 (찌른 곳에는 칼이 남아있어야 한다)



import random as ran
import sys
hole = list(range(1, 11))
fire = ran.sample(hole, 3)

while len(hole) > 0:
    user = int(input('숫자를 선택해주세요> '))
    if user in hole:
        if user in fire:
            hole.remove(user)
            print('아져씨가 발사됬습니다!')
            print(f'남은 숫자들은 {hole} 입니다.')
        else:
            hole.remove(user)
            print('아무런 반응이 없었습니다.')
            print(f'남은 숫자들은 {hole} 입니다.')
    elif user not in hole:
        print('잘못된 입력입니다.')
    if len(fire) == 0 and len(hole) > 0:
        print('통아저씨의 승리입니다.')
    break
    if (len(fire) == 3 and len(hole) == 3) or  (len(fire) == 2 and len(hole) == 4) or (len(fire) == 1 and len(hole) == 5):
        print('사용자의 승리입니다.')
    break


