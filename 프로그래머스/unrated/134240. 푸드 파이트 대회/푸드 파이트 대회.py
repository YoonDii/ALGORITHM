def solution(food):
    answer = ''
    for i in range(1,len(food)):
        n = food[i]//2 #2로 나눠지는 몫만 가져오기 
        answer += str(i) * n #몫만큼 음식배치하기
    answer = answer + '0' + answer[::-1] #물을 기준으로 양쪽으로 대칭되게 만들기
    return answer