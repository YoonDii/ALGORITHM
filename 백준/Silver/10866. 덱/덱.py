from collections import deque
import sys

n = int(sys.stdin.readline())

d = deque()

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push_front":
        d.appendleft(a[1])

    elif a[0] == "push_back":
        d.append(a[1])

    elif a[0] == "pop_front":
        if d:
            print(d.popleft())

        else:
            print(-1)

    elif a[0] == "pop_back":
        if d:
            print(d.pop())

        else:
            print(-1)
    elif a[0] == "size":
        print(len(d))

    elif a[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif a[0] == "back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])