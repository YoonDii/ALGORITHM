def solution(my_string):
    # my = set(my_string)
    # print(my){'p', 'l', 'e', 'o'}
    
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer
    
    