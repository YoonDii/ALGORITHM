N = int(input())
arr = []
for i in range(N):
    a, b = input().split()
    a = int(a)
    arr.append([a, b])
arr.sort(key=lambda x: x[0])

for i in arr:
    print(*i)