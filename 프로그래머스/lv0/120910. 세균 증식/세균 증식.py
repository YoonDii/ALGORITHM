# def solution(n, t):
#     result = n
#     for i in range(t):
#         result *= 2
#     return result
        
    
def solution(n, t):
    answer = n * (2 ** t)
    return answer