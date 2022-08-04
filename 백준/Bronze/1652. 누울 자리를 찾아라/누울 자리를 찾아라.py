import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(str,input().rstrip()))for _ in range(n)]

sleep = [0,0]
# r = 행 
# c = 열 
for i in range(n):
    r , c = 0 , 0 #'.'이 연속하는지 알기위해서 선언
    for j in range(n):
        if room[i][j] == '.': #[행][열] 가로 구하기
            r += 1
        else:
            r = 0
        if r == 2: #두칸 연속이면 잘수있음.
            sleep[0] += 1
        
        if room[j][i] == '.':#[열][행] 세로구하기.
            c += 1
        else:
            c = 0
        if c == 2:
            sleep[1] += 1
        
print(*sleep)