def solution(num_list):
    answer = 0
    evl = "";
    odd = "";
    
    for i in num_list :
        if i % 2 == 0:
            evl += str(i)
        else:
            odd += str(i)
    
    answer = int(evl) + int(odd)
    return answer