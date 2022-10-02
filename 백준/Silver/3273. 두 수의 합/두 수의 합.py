import sys

input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))  # 정렬필수!
x = int(input())

answer = 0
start, end = 0, n - 1  # 왼쪽, 오른쪽

while start < end:
    temp = nums[start] + nums[end]
    if temp == x:
        answer += 1
        start += 1  # 범위 오른쪽으로 줄여가기
    elif temp < x:
        start += 1
    else:
        end -= 1  # 범위 왼쪽으로 줄여가기, 제일 큰것 보다 작기때문에 더 작은수를 봐야함
print(answer)
