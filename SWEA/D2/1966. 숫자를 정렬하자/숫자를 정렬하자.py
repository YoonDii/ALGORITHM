t = int(input())


for tc in range(1, t + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = ""

    for i in nums:
        ans += str(i)
        ans += " "

    print(f"#{tc} {ans}")
    