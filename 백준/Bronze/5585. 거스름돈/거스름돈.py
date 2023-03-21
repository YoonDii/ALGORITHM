money = int(input())

# 잔돈으로 받은 돈
ans = 1000 - money
cnt = 0

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    cnt += ans // coin
    ans %= coin
print(cnt)
