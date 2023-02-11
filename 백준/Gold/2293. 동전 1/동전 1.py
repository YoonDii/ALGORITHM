n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1

for c in coins:  # 리스트에 동전을 하나씩 돌면서
    for i in range(c, k + 1):  # c원 동전으로 i원 만들기 / i-c원을 만든 후 c원 추가하는것
        result = dp[i - c]
        dp[i] += result # 동전들 다 더한 경우

print(dp[k])