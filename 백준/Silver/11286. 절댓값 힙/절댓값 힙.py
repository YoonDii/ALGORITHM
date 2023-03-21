import sys
import heapq

x = int(sys.stdin.readline())
q = []

for i in range(x):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
