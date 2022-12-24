def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass

    return answer
    