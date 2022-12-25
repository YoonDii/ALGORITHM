def solution(cipher, code):
    result = ''
    for i in range(code,len(cipher)+1):
        if i % code == 0 :
            # print(i)
            result += cipher[i-1]
    return result
    
            
            