import sys
input=sys.stdin.readline

n = int(input())

nums = []

for i in range(n):
    a, b, = map(int,input().split())
    nums.append((a,b))
# print(nums) [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]

nums.sort(key= lambda x : (x[1],x[0]))

for i in nums:
    print(*i)