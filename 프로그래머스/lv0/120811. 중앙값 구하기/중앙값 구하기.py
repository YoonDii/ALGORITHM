def solution(array):
    array.sort(reverse=False)
    x = len(array) // 2
    return array[x]