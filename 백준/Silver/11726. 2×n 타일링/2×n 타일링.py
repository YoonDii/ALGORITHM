n = int(input())

dp = [0] * 1001  # (1 ≤ n ≤ 1,000)
# n이 1,2인 경우는 확정
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
