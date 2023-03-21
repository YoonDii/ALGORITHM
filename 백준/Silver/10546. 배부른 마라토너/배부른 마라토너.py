n = int(input())

runners = {}

for i in range(n):
    name = input()
    if name in runners:
        runners[name] += 1
    else:
        runners[name] = 1

for i in range(n - 1):
    name = input()
    if runners[name] == 1:
        del runners[name]
    elif name in runners:
        runners[name] -= 1
print(*runners)