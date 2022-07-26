win = 0     #우승자 초기화
total = 0   #총점 초기화
for i in range(5):  #입력값이 5줄 나오게하기.
    a, b, c, d = map(int,input().split())  #입력값
    if total < a + b + c + d:   # 총점이 현재는 0이라서 입력값이 무조건 큼.
        win = i + 1             # 초기화값이 0이라서 i에 1을 더해줌.
        total = a + b + c + d   # 총점 구하기
print(win ,total)