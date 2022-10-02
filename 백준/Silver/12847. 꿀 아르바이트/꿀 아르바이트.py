n, m = map(int, input().split())
money = list(map(int, input().split()))


# print(money)[10, 10, 20, 20, 30]

sum = 0
for i in range(m):
    sum += money[i]

start = 0  # 인덱스 기준
end = m  # 일할수있는날
msum = sum  # 변수 다시 정의

while end < n:
    sum = sum + money[end] - money[start]
    msum = max(msum, sum)
    start += 1
    end += 1
print(msum)