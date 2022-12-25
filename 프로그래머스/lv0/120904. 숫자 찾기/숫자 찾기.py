def solution(num, k):
    answer = 0
    lis = list(str(num))

    for i in range(len(lis)):
        if lis[i] == str(k):
            return i + 1

    return -1