import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀허용 깊이를 수동으로 늘려주는 코드

#n = 정점의 수, m = 간선의 수 , r = 시작 정점
n, m, r = map(int,input().split())
graph = [[]for _ in range(n+1)] # 연결노드 그래프 /1번노드와 인덱스 값이 같게 하기 위해서 n+1
visited = [0] * (n+1) #방문순서 그래프 /인덱스값과 같게하기 위해 n+1
count = 1 

#연결된 노드 입력 받기
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v): #방문했는지 알아보기
    global count #함수 밖에 count값을 쓰기 위해서 global명시
    visited[v] = count #방문할 때마다 순차 값 변경
    graph[v].sort(reverse= True) #내림차순
    for i in graph[v]: #연결된 노느 방문
        if visited[i] == 0: # 방문 안한 노드일 경우
            count += 1 #순차 증가
            dfs(i) #함수실행

dfs(r) #시작정점 r

for i in range(1,n+1):# 순차 출력
        print(visited[i])