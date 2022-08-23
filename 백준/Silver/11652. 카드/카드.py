import sys
input = sys.stdin.readline

d = dict()
for _ in range(int(input())):
    n = int(input()) 
    if d.get(n):
        d[n] += 1
    else:
        d[n] = 1
        
ans,max_cnt = 0,0

lst = sorted(d.items())
for num, cnt in lst:
    if max_cnt < cnt:
        max_cnt = cnt
        ans = num
print(ans)
