a, b = map(int, input().split())

nums_1 = set(map(int, input().split()))
nums_2 = set(map(int, input().split()))

print(len(nums_1 - nums_2))
print(*sorted(list(nums_1 - nums_2)))