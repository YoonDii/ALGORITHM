def solution(s):
    answer = ''
    for aph in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(aph) == 1:
            answer += aph
    return answer