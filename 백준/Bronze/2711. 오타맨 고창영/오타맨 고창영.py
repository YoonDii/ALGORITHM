t = int(input())

for i in range(t):
    m ,n = input().split()
    m = int(m)
    print(n[:m-1], n[m:], sep='')
