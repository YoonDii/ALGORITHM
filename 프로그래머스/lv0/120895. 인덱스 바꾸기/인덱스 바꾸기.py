def solution(my_string, num1, num2):
    answer = ''
    my = list(my_string)
    my[num1],my[num2] = my[num2],my[num1]
    return answer.join(my)