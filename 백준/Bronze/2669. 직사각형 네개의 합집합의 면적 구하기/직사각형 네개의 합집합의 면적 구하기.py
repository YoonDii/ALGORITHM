import sys
input = sys.stdin.readline

squ = [[0]*101 for a in range(101)] #모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

for a in range(4):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(x1,x2): #가로
        for j in range(y1,y2): #세로
            squ[i][j] = 1
print(sum(sum(squ,[]))) # 그려진 사각형면적을 다 합치기.