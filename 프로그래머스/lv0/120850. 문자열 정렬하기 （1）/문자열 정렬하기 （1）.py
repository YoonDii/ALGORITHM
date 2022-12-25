def solution(my_string):
    answer = []
    nums = '0123456789'
    
    for i in my_string:
        if i in nums:
            answer.append(int(i))
            answer.sort()
                      
    return answer
            