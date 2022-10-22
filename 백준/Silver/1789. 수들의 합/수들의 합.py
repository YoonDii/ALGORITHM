s = int(input()) # 최대값 200

n = 1 # 자연수 n
sum = 0 # 합계

while True :
    sum += n # sum = n + sum
    if sum > s :
        print(n-1) # 합계가 더 클 경우 N에서 1을 뺀 값 출력
        break
    elif sum == s : # 합계와 S의 값이 같으면 N 그대로 출력
        print(n)
        break
    n += 1 # 조건에 만족하지 않을 때 1씩 더하기