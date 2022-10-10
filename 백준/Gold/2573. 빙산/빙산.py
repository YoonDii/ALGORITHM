import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):  # 빙하 주변의 바다의 갯수 파악 
    visit[a][b] = True
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                elif not maps[nx][ny]:
                    water[x][y] += 1
    return 1


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

year, flag = 0, 0

while True:
    visit = [[0] * m for _ in range(n)]
    water = [[0] * m for _ in range(n)]
    land_cnt = 0

    for i in range(n):
        for j in range(m): # 모든 매트릭스를 찾으며 빙하가 존재 할 때  바다를 bfs를 통해 델타탐색 진행 
            if maps[i][j] and not visit[i][j]:
                bfs(i, j)
                land_cnt += 1
    for i in range(n):
        for j in range(m):
            maps[i][j] -= water[i][j] # 빙하의 높이에다가 찾아낸 바다의 카운팅의 값을 빼준다.
            if maps[i][j] < 0:
                maps[i][j] = 0
    if land_cnt == 0: #빙하가 0개일때 
        break
    if land_cnt >= 2: # 빙하가 2개일때 
        flag = 1
        break
    year += 1 # 두 조건문을 안걸리면  연도 증가
if flag:
    print(year)
else:
    print(0)