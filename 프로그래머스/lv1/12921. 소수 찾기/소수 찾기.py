def solution(n):
    num = set(range(2,n+1))
    # print(num){2, 3, 4, 5, 6, 7, 8, 9, 10} 
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
            # print(num){2, 3, 5, 7}
    return len(num)