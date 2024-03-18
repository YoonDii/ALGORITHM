def solution(a, b):
    one = int(str(a)+str(b))
    two = 2*int(a)*int(b)
    print(one,two)
    answer = ''
    if one > two :
        answer = one
    elif one ==two :
        answer = one
    else:
        answer = two
    return answer