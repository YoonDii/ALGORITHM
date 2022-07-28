N , M = map(int,input().split())
#sasa모형은 각 블럭이 2개씩 필요.
#두 블럭을 2로 나눴을때 적게 나오는 블럭의 몫이 sasa모형을 만들 수 있는 최대값.
S = (N // 2)
A = (M // 2)

print(min(S,A))