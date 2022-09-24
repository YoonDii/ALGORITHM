import sys
input=sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    a, b = map(int,input().split())
    nums.append((a,b))
    # print(nums) [(3, 4), (1, 1), (1, -1), (2, 2), (3, 3)]

nums.sort(key= lambda x : (x[0],x[1]))

for i in nums:
    print(*i)