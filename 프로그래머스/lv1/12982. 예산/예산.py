def solution(d, budget):
    sd = sorted(d) # 먼저 정렬을 한다
    answer = 0
    for i in sd:
        budget -= i # 예산에서 부서별지원금빼기
        if budget < 0: #0보다 작아진다면 더하지 않고 멈추기
            break
        answer += 1 # 0보다 작지않다면 1씩더해주기
    return answer # 예산이 모자르기 전에 지원한 부서의 개수
    
        
        
   