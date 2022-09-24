import sys
input=sys.stdin.readline

n = int(input())
nums = [0]* 10001

for i in range(n):
    nums[int(input())] += 1

for i in range(1,10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)
