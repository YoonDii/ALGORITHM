t = int(input())


for _ in range(t):
    n, m = map(int,input().split())
    cnt = 0
    for i in range(n, m+1):
        nums = str(i)
        #print(nums)
        cnt += nums.count('0')
    print(cnt)