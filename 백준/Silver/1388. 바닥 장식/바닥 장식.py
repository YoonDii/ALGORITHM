n, m = map(int, input().split())  # 세로,가로
wood = [input() for _ in range(n)]
cnt = 0

for i in range(n):
    j = 0
    while j < m:
        if wood[i][j] == "|":
            j += 1
        else:
            cnt += 1
            while j < m and wood[i][j] == "-":
                j += 1

for j in range(m):
    i = 0
    while i < n:
        if wood[i][j] == "-":
            i += 1
        else:
            cnt += 1
            while i < n and wood[i][j] == "|":
                i += 1
print(cnt)
