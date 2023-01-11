t = int(input())

dp = [0] * 11

dp[1],dp[2],dp[3] = 1,2,4

for _ in range(t):
    n = int(input())
    if n == 1 or n == 2 or n ==3:
        print(dp[n])
    else:
        for i in range(4,n+1):
            dp[i] = dp[i-1]+ dp[i-2] + dp[i-3]

        print(dp[n])