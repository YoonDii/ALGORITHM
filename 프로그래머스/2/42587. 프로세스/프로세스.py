def solution(priorities, location):
    answer = 0
    
    here = priorities.index(max(priorities))
    
    while True:
        i = max(priorities)
        if priorities[here] == i:
            priorities[here] = 0
            answer += 1
            
            if here == location :
                break
        here += 1
        if here >= len(priorities):
            here = 0    
    
    return answer
        