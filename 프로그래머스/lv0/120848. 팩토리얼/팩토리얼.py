def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = factorial * answer
    answer -= 1
    return answer