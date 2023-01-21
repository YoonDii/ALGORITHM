
n = int(input())


for tc in range(1, n + 1):
    nums = list(map(int, input().split()))

    nums.sort()
    nums.remove(nums[0])
    nums.remove(nums[-1])

    total = sum(nums)
    ans = round(total / len(nums))
    print(f"#{tc} {ans}")