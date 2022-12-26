def solution(emergency):
    answer = []
    sort_num = sorted(emergency, reverse = True)

    for i in emergency:
        answer.append(sort_num.index(i) + 1)

    return answer