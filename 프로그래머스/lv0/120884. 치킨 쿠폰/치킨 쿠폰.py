def solution(chicken):
    result = 0
    
    while chicken >= 10:
        answer = chicken//10 
        result += answer 
        chicken = chicken%10 + answer 
    return result 