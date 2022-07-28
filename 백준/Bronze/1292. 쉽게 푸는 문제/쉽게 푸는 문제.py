a, b = map(int,input().split())

nums = []

for i in range(1,1001): #수열범위를 어떻게 구할지 몰라서,,1000까지 범위설정
    for x in range(i):
        nums.append(i)
print(sum(nums[a-1:b])) # 0을 제외하고 더해주기 위해서 a-1부터 설정
