def solution(n):
    num = []
    for i in range(1,n+1):
        if n % i == 1 :
            num.append(i)
            print(i)
            return i
    # answer = min(num)
    # return answer
    