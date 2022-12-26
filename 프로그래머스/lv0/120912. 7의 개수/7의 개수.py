def solution(array):
    array = str(array)
    answer = 0
    for i in range(len(array)):
        if array[i] == '7':
            answer += 1
    return answer