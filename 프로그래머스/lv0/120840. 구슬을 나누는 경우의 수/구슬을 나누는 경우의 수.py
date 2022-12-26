def solution(balls, share):
    answer = 1
    for i in range(balls - share + 1, balls + 1) :
        answer *= i
    for j in range(2, share + 1) :
        answer /= j
    return int(answer)