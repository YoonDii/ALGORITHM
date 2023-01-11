n = int(input())

nums = list(map(int, input().split()))
# print(nums)[10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
# sort_nums = sorted(nums)
# print(sort_nums)[-35, -4, -1, 1, 3, 5, 6, 10, 12, 21]

for i in range(1, n):
    nums[i] = max(nums[i], nums[i - 1] + nums[i])
    # i가 돌아가면서 더 큰 수로 바뀜
print(max(nums))