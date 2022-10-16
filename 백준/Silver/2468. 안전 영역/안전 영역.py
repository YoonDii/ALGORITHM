
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# (-1,0)(1,0)(0,1)(0,-1)

def dfs(x, y, h):

    for m in range(4):#사방탐색
        nx = x + dx[m]
        ny = y + dy[m]

        # 범위를 벗어나지않도록 조건 주기
        if (0 <= nx < N) and (0 <= ny < N) and not visit[nx][ny] and zone[nx][ny] > h:
            visit[nx][ny] = True
            dfs(nx, ny, h)


N = int(input())
zone = [list(map(int, input().split())) for _ in range(N)]

ans = 1
for k in range(max(map(max, zone))):
    visit = [[False] * N for _ in range(N)]
    safe = 0

    for i in range(N):
        for j in range(N):
            if zone[i][j] > k and not visit[i][j]:
                safe += 1
                visit[i][j] = True
                dfs(i, j, k)
    ans = max(ans, safe)

print(ans)