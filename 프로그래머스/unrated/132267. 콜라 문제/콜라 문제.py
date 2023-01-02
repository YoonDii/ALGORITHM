def solution(a, b, n):
    answer = 0
    while n//a*b > 0:
        e = (n // a) * b
        answer += e
        n = e + (n % a)
        
    return answer