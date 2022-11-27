n, m = map(int, input().split())
a, b = [], []
for i in [a, b]:
    for j in range(n):
        i.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(*a[i])