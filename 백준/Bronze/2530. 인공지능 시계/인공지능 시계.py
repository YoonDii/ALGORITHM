a, b, c = map(int, input().split())  # 시,분,초
d = int(input())  # 요리시간


c += d
b += c // 60
a += b // 60
print(a % 24, b % 60, c % 60)
