def solution(price, money, count):
    answer = 0
    
    for i in range(1,count+1):
        answer += price * i
    # print(answer) 30
        
    if money < answer :
        result = answer - money
        return result
    else:
        return 0
    

    