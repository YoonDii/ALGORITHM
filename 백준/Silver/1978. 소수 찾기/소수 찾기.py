n = int(input())
nums = list(map(int,input().split()))
result = 0

for i in nums:
    cnt = 0
    if i == 1:#1은 소수가 아니기 때문에 건너뜀
        continue
    for j in range(2,i+1): #1을 건너뛰었으니 2번부터 돌자!
        if i % j == 0: #소수찾기
            cnt += 1
           
    if cnt == 1: #cnt가 1이 되면
        result +=1 #소수 갯수 추가
print(result)
