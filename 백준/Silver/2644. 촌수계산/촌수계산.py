import sys
sys.setrecursionlimit(10000) 
input = sys.stdin.readline

n = int(input())
start ,end = list(map(int,input().split()))
m = int(input())

graph  = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

stack = []
stack.append((start, 0)) #기본값 설정 / 스택에 값을 추가할때 촌수도 같이 추가한다.튜플로 값입력
visited[start] = True #시작하는곳이여서 트루

ans = -1 #정답을 출력할 변수 / 촌수가 연결되어있지 않으면 -1출력

while len(stack) != 0: #스택이 비여있지 않으면 반복
    num , cnt = stack.pop() #값과 촌수
    
    if num == end:# end값과 같으면 멈추기
        ans = cnt 
        break

    for i in graph[num]:
        if not visited[i]:# 방문을 안했으면
            visited[i] = True #방문표시하고
            stack.append((i, cnt+1)) #스택에 넣기 / 촌수는 증가해야하기때문에 +1

print(ans)