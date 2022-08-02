n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))
s_nums = sorted(nums)
#print(s_nums)
for i in range(len(s_nums)):
    #print(len(nums))
    print(s_nums[i])