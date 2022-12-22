def solution(money):
    if money:
        a =  money//5500
        b = money - (5500*a)
    return [a,b]
    
        
        