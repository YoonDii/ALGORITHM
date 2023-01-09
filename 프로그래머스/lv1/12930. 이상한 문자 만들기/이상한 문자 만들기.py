def solution(s):
    answer = ''
    i = 0
    for words in s:
        if words == ' ':
            answer += words
            i = 0
        else:
            if i % 2 == 0:
                answer += words.upper()
            else:
                answer += words.lower()
            i += 1
    return answer