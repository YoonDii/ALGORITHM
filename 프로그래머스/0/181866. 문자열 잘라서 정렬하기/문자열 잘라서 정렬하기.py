def solution(myString):
    answer = []
    # for i in range(len(myString)):
    #     if myString[i] != 'x':
    #         answer.append(myString[i])
    
    for i in myString.split('x'):
        if i :
            answer.append(i)
    return sorted(answer)