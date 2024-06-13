import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 인접 리스트를 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS
def dfs(graph, start):
    visited = set()
    stack = [start]
    route = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            route.append(node)
            # 인접 노드를 역순으로 스택에 추가 (작은 숫자부터 방문하기 위해)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return route

# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    route = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            route.append(node)
            # 인접 노드를 큐에 추가
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return route

dfs_route = dfs(graph, V)
bfs_route = bfs(graph, V)

print(*dfs_route)
print(*bfs_route)
