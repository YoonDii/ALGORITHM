P = [0] * 101
# 3까지는 1로 확정
P[1] = 1
P[2] = 1
P[3] = 1
for i in range(4, 101):
    P[i] = P[i - 3] + P[i - 2]
    # 삼각형이 4개일때부터 수가 증가
    # P[4]=P[1]+P[2] =2

t = int(input())
for i in range(t):
    n = int(input())
    print(P[n])
