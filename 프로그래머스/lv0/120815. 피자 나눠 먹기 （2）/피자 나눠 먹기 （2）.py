def solution(n):
    answer = 6
    while (answer%n) != 0:
        answer += 6

    return answer/6