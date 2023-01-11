def solution(quizes):
    answer = []
    for quiz in quizes:
        qlist = quiz.split()
        if qlist[1] == '+':
            if int(qlist[4]) == int(qlist[0]) + int(qlist[2]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(qlist[4]) == int(qlist[0]) - int(qlist[2]):
                answer.append('O')
            else:
                answer.append('X')
    return answer