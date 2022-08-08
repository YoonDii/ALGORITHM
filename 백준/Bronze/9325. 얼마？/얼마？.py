t = int(input())

for _ in range(t):
    s = int(input())
    for _ in range(int(input())):
        q, p = map(int, input().split())
        s += q*p
    print(s)