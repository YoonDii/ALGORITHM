def solution(survey, choices):
    answer = ''
    scores = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0 }
    add_score = {1:3, 2:2, 3:1, 4:0, 5:-1, 6:-2, 7:-3}

    for i in range(len(survey)):
        scores[survey[i][0]] += add_score[choices[i]]

    if scores["R"] >= scores["T"]:
        answer += "R"
    else:
        answer += "T"
    if scores["C"] >= scores["F"]:
        answer += "C"
    else:
        answer += "F"
    if scores["J"] >= scores["M"]:
        answer += "J"
    else:
        answer += "M"
    if scores["A"] >= scores["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer