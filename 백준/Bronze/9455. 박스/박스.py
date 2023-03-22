t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    box = [input().split() for _ in range(m)]

    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(m - 1, -1, -1):
            if box[j][i] == "1":
                ans += cnt
            else:
                cnt += 1
    print(ans)
