def solution(common):
    answer = 0
    if (common[0] + common[2]) / 2 == common[1]:
        gap = common[1] - common[0]
        answer = common[-1] + gap
    else:
        gap = common[1] / common[0]
        answer = common[-1] * gap
    return answer