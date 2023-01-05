import sys
from collections import deque
input=sys.stdin.readline

# n=정점개수, m=간선개수, v=탐색시작점
N, M, V = list(map(int, input().split()))

# 인접영행렬
matrix = [[0]*(N+1) for i in range(N+1)]

#방문한곳체크기록할 리스트
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

# 입력받는 값에 대해 영형렬에 1삽입(인접리스트생성)
for i in range(M):
  a,b=map(int,input().split())
  matrix[a][b]=matrix[b][a]=1

def dfs(V):
  visited_dfs[V]=1
  print(V,end=' ')
  #재귀
  for i in range(1, N+1):
    if(visited_dfs[i]==0 and matrix[V][i]==1):
      dfs(i)

def bfs(V):
  #방문해야할 곳을 순서대로 넣을 큐
  queue=deque([V])
  visited_bfs[V]=1
  
  #큐안에 데이터없을때까지
  while queue:
    V=queue.popleft()
    print(V, end=' ')
    for i in range(1, N+1):
      if(visited_bfs[i]==0 and matrix[V][i]==1):
        queue.append(i)
        visited_bfs[i]=1

dfs(V)
print()
bfs(V)