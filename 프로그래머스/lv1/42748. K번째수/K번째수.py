def solution(array, commands):
    answer = []
    for i in commands:
        arr = array[i[0]-1:i[1]]
        # print(arr)[5, 2, 6, 3] [6] [1, 5, 2, 6, 3, 7, 4]
        
        arrs = sorted(arr)
        # print(arrs)[2, 3, 5, 6] [6] [1, 2, 3, 4, 5, 6, 7]
        
        result = arrs[i[2]-1]
        # print(result) 5 6 3
        answer.append(result)
    return answer