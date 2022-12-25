def solution(array):
    result = []
    maxnum = max(array)
    for i in array:
        if i == maxnum :
            result.append(i)
            idx = array.index(maxnum)
            result.append(idx)
    return result
            
            
            
  
    