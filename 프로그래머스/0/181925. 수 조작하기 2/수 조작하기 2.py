def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        if numLog[i]-numLog[i-1] == 1:
            answer += 'w'
        if numLog[i-1]-numLog[i] == 1:
            answer += 's'
        if numLog[i]-numLog[i-1] == 10:
            answer += 'd'
        if numLog[i-1]-numLog[i] == 10:
            answer += 'a'
    return answer