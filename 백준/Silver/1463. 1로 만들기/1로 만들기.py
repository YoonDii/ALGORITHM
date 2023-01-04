x = int(input())  # 수 입력받기
d = [0] * (x + 1)
# 1-based /1번째 수는 사실 d[1]이 아니고 d[2]이기 때문에, 계산하기 편하게 d[1]을 1번째 인 것 처럼 만들어준다.

for i in range(2, x + 1):  # 2부터 x까지 반복/ 1보다 크거나 같은 x
    # print(i)(2,3,4,5,6,7,8,9,10)
    d[i] = d[i - 1] + 1  # 1을 빼는 연산 -> 1회 진행
    if i % 2 == 0:  # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:  # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i] = min(d[i], d[i // 3] + 1)
print(d[x])  # 3가지 연산을 다 실행해보고 최솟값을 구하는것.