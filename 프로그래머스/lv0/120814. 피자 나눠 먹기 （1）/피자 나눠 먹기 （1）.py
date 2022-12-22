def solution(n):
    if n % 7 == 0: 			#1
        answer = n // 7		#2
    else:
        answer = n // 7 + 1 #3
    return answer
        