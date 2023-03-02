x = int(input())
n = int(input())

ans = 0
for i in range(n):
    cash = list(map(int, input().split()))
    money = cash[0] * cash[1]

    if money:
        ans += money
if x == ans:
    print("Yes")
else:
    print("No")