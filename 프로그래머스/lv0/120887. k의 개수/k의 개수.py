def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        if str(k) in str(num):
            answer += str(num).count(str(k))
    return answer