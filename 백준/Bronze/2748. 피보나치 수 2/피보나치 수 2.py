n = int(input())

arr = [0 for _ in range(n + 1)]
# print(arr) [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 값을 저장해줄 리스트만들기
arr[1] = 1
# print(arr) [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다 (문제에 나와있음)

for i in range(2, n + 1):  # 문제에서 n>=2라고 나와있음
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[-1])  # 마지막 수 꺼내기