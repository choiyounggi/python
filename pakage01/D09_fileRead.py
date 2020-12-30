with open('result/test01.txt', 'r', encoding='utf8') as f:
    # f.readable() : 읽을 수 있는 객체라면 True..
    while True:
        # f.readline() : 파일 내용을 한 줄씩 읽기
        line = f.readline()
        
        # 할 줄을 읽었을 때 길이가 0이라면 그만 읽기
        if len(line) == 0:
            break
        else:
            print(line, end='')

with open('result/test01.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        print('2번째 read:', line, end='')

with open('result/test01.txt', 'r', encoding='utf8') as f:
    data = f.read()
    print('3번째 read:', data)
    
    # 전체 데이터를 가져와서 \n으로 split하는 것은
    # readlines와 같다
    for line in data.split(seq='\n'):
        print('4번째 read:', line)
    