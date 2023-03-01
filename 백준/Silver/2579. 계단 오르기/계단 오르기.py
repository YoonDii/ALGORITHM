n = int(input())

# 계단의 개수는 300이하의 자연수
stair = [0 for _ in range(301)]  # 점수 리스트 받기
dp = [0 for _ in range(301)]  # 점수의 합 리스트

for i in range(n):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])  # 연속된계단, 한칸뛰어넘은계단 둘 중 더 큰 합을 선택

for i in range(3, n):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])
print(dp[n - 1])
