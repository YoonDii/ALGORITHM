n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))
    
nums.sort()
for num in nums:
    print(num)