n = int(input())

ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += b % a # 나머지 다 더해주기
print(ans)
