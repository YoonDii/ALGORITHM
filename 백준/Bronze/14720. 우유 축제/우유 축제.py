t = int(input())
milk = list(map(int,input().split()))

cnt = 0

for m in range(t): #우유가게 개수만큼 반복
    if milk[m] == cnt % 3: #milk리스트순서가 cnt를 3으로 나눈 나머지와 같으면 +1. 0나누기3은 나머지 0. 1나누기3은 나머지 1.
        cnt += 1
print(cnt) 
