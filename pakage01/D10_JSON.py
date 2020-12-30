# 데이터를 json형식의 문자열로 변환(encoding)/복원(decoding)해주는 모듈

import json

record = {
    'win': 5000,
    'draw': 3800,
    'lose': 4355
}

jsonStr = json.dumps(record)
print(jsonStr)

with open('record.json', 'w') as f:
    f.write(jsonStr)

with open('record.json', 'r') as f:
    data = f.read()
    loaded = json.loads(data)

    print(loaded['win'])
    print(loaded['draw'])
    print(loaded['lose'])