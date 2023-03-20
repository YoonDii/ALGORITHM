def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer


#a와 b를 어떻게 곱해야하나 생각했다.
#a와b를 각각 인덱스를 하나식 구해야하는 줄 알았다.
# 일단은 a와b의 길이가 같아서 a의길이만 for문으로 돌려주었다.