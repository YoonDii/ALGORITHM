def solution(array, height):
    answer = 0
    array.sort(reverse=False)
    for i in range(len(array)):
        if array[i] >height:
            answer += 1
        else :
            continue
    return answer