def solution(my_string):
    arr = my_string.split()
    # print(arr)['3', '+', '4']
    answer = int(arr[0]) 

    for i in range(1, len(arr), 2):
        if arr[i] == "+":
            answer += int(arr[i+1]) 
        else:
            answer -= int(arr[i+1])

    return answer