import sys

input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    a = input().split()

    if a[0] == "push":
        stack.append(a[1])
        # print(stack)

    elif a[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif a[0] == "size":
        print(len(stack))

    elif a[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif a[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
