from collections import deque

n, k = map(int, input().split())

ysps = []  # 뽑은 수 넣을 요세푸스리스트

queue = deque()

for i in range(1, n + 1):
    queue.append(i)
# print(queue)[1, 2, 3, 4, 5, 6, 7]

while queue: 
    for i in range(k - 1):
        queue.append(queue.popleft())
    ysps.append(queue.popleft())

print("<", end="")
print(", ".join(map(str, ysps)), end="")
print(">")