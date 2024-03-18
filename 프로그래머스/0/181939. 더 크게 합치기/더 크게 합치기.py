def solution(a, b):
    one = str(a)+str(b)
    two = str(b)+str(a)
    if int(one) > int(two):
        answer = one
        
    else:
        answer = two
    return int(answer)