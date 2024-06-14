
from collections import deque
N,M = list(map(int,input().split()))
graph=[]
for _ in range(N):
    ans = list(map(int,input()))
    graph.append(ans)

dy = 1, -1, 0, 0
dx = 0, 0, -1, 1

start = (0,0,1)
queue = deque()
queue.append(start)

visit = set()
visit.add(start)

while queue:
    y,x,cnt = queue.popleft()
    #  값이 있던 없던 출구면 stop
    if (y == N - 1) and (x == M - 1):
        print(cnt)
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if graph[ny][nx] != 1:
            continue
        if (ny,nx) in visit:
            continue
        queue.append((ny,nx,cnt+1))
        visit.add((ny,nx))



