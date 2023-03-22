def solution(arr):
    answer = []
    x = -1
    for i in arr:
        if i != x:
            x = i
            answer.append(i)

    return answer