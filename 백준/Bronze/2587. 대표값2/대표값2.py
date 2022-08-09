nums = []
for i in range(5):
    nums.append(int(input()))
    nums.sort()
    #print(nums) #[10, 30, 30, 40, 60]

print(sum(nums)//5)
print(nums[2])
