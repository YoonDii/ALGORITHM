n, m = map(int, input().split())
ball = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())

    for x in range(i, j + 1):
        ball[x - 1] = k

print(*ball)