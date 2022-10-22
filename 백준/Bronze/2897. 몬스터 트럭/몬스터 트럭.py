# R 행(가로), C 열(세로)
R, C = map(int, input().split())

parking = [list(input()) for _ in range(R)]
# print(parking)
# (y,x)
# 우하좌본인
dx = [0, 0, 1, 1]  # R
dy = [0, 1, 1, 0]  # C

monster = [0] * 6  # 정답출력리스트

for i in range(R - 1):  # 인덱스범위
    for j in range(C - 1):
        car = 0
        # i = 0
        # j = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < R and 0 <= ny < C:  # 범위를 줘야된다 벗어나지않게
                x = nx
                y = ny

                if parking[x][y] == "#":
                    car = 5
                    break  # 빌딩이 있으면 주차를 못하고 나가기
                elif parking[x][y] == "X":
                    car += 1
        monster[car] += 1
for i in range(5):
    print(monster[i])
