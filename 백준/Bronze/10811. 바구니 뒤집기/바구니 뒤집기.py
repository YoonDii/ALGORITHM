n, m = map(int, input().split())
ball = [(i + 1) for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    ball[i - 1 : j] = reversed(ball[i - 1 : j])
print(*ball)