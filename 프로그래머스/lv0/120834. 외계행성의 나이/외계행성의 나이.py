def solution(age):
    answer = ''
    alpha = 'abcdefghij'
    for i in str(age):
        answer += alpha[int(i)]
    return answer
