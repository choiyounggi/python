# 중복되지 않는 랜덤숫자 6개를 뽑아보세요 (1 - 45)

import random

lotto = set(range(1, 46))
lottoNum = random.sample(lotto, 6)

print('로또 번호는: ', lottoNum)