chess = [list(input()) for _ in range(8)]

cnt = 0
for i in range(8):
    for x in range(8):
        if i % 2 == 1 and x % 2 == 1 and chess[i][x] == "F":
            cnt += 1
        if i % 2 == 0 and x % 2 == 0 and chess[i][x] == "F":
            cnt += 1
print(cnt)