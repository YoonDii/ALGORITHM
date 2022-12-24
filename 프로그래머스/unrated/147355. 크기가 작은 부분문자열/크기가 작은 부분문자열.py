def solution(t, p):
    result = 0
    t_list = []
    for i in range(0,len(t)):
        if len(t[i:i+len(p)]) == len(p):
            t_list.append(t[i:i+len(p)])
            # print(t_list)
            
    int_t_list = list(map(int,t_list))
    # print(int_t_list) [314, 141, 415, 159, 592]
    
    for t in int_t_list :
        if t <= int(p):
            result += 1
            # print(t,p)
    return result