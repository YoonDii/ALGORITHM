from collections import deque


n = int(input())
queue = deque()

for i in range(n):
    queue.append(i + 1)  # 카드 넣어주기

while len(queue) > 1:  # 카드가 1개라도 들어있으면
    queue.popleft()  # 먼저들어온거빼주기
    queue.append(queue.popleft())  # 빼준거 다시 넣어주기

print(queue.pop())  # 마지막남은카드