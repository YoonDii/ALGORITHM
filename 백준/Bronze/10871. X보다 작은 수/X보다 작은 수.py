n, x = map(int,input().split())
nums = list(map(int,input().split()))
# print(nums) [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
num = []
for i in nums:
    if i < x :
        num.append(i)
print(*num)
