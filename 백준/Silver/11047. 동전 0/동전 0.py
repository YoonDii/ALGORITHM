n, k = map(int, input().split())
a = [0] * n  # 동전 리스트
# print(a)[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    a[i] = int(input())
# print(a) [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
cnt = 0

for i in range(n-1, -1, -1):  # 역순으로 반복 / 가격이 큰 동전부터 선택해야 개수를 최소로 할수있음.
    if a[i] <= k:  # k보다 동전 가치가 작거나 같으면 cnt에 추가
        cnt += int(k / a[i])
        k = k % a[i]  # k를 현재 동전을 사용하고 남은 금액으로 갱신
print(cnt)