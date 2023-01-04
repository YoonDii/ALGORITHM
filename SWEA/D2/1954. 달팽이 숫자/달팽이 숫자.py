t = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, t + 1):
    n = int(input())
    data = [[0] * n for _ in range(n)]
    # 초기 위치 및 회전 방향 정의
    x, y = 0, 0
    direction = 0

    for j in range(1, n * n + 1):
        data[x][y] = j
        x += dx[direction]
        y += dy[direction]

        if not 0 <= x < n or not 0 <= y < n or data[x][y] != 0:
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    print("#%d" % i)
    for j in range(n):
        for k in range(n):
            print(data[j][k], end=" ")
        print()