def solution(num_list):
    answer = 0
    num1 = 1;
    num2 = 0;
    
    for i in num_list :
        num1 *= i
        num2 += i

    if int(num1) < int(num2**2):
        answer = 1
    else:
        answer = 0
    
    return answer