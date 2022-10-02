import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, c):
    visit[a][b] = True
    graph[a][b] = c
    cnt = 1
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if graph[nx][ny] == "1":
                    visit[nx][ny] = True
                    graph[nx][ny] = c
                    cnt += 1
                    queue.append((nx, ny))
    return cnt
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

v_cnt = 0
ans = []
color = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and not visit[i][j]:
            ans.append(bfs(i, j, color))
            v_cnt += 1
            color += 1
print(v_cnt)
ans.sort()
print(*ans, sep="\n")