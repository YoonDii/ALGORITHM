def solution(my_string, n):
    result = []
    for i in range(len(my_string)):
        for j in range(n):
            result.append(my_string[i])
    return "".join(result)
        