import sys
sys.setrecursionlimit(10000) 
input = sys.stdin.readline

n,m = map(int,input().split())
graph=[[] for _ in range(n+1)] #1부터 시작하기 위해서 +1
visited=[False]*(n+1) #방문여부확인
result=0

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]: #방문하지 않았으면 반복
            dfs(i)

for i in range(1,n+1):#1부터 시작하기위해서
    if not visited[i]: #방문하지않았으면 반복하고
        dfs(i)
        result+=1 # 하나 더해주기.
print(result)
