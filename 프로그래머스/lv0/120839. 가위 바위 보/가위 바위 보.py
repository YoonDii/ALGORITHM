def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += "0"
        elif i == '5':
            answer += '2'
        else :
            answer += '5'
       
    return answer