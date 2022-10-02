import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = [0]
numsum = 0
for i in range(n):
    numsum += nums[i]  # 리스트 인자값 순서대로 더하기/ 누적합 먼저 구해주기
    arr.append(numsum)  # 더한값 새로운 리스트에 넣어주기
# print(arr)[0, 5, 9, 12, 14, 15]

for x in range(m):
    i, j = map(int, input().split())  # 인덱스 값 받기
    print(arr[j] - arr[i - 1])  # 큰수에서 작은수 빼서 값구하기
