def solution(arr):
    answer = []
    for i in range(len(arr)):
        for x in range(arr[i]):
            answer.append(arr[i])
    return answer