def solution(nums):
    answer = 0
    for i in range(0, len(nums)-2): #3개의수만 더해야함
        for j in range(i+1, len(nums)-1):#i의 다음 수부터 i를 뺀 개수
            for k in range(j+1, len(nums)):#j의 다음 수부터 i,j를 뺀 개수
                sum_num = nums[i] + nums[j] + nums[k] #3개의 수 합
                 
                for x in range(2, round(sum_num/2)): #더한 수가 소수인지 확인하기
                    #정수 n을 2로 나누어 2부터 n/2 까지의 정수로 모두 나누어 확인
                    if sum_num % x == 0: #소수가 아니면 개수 안세기
                        break
                else:
                    answer += 1 #소수면 개수세기
    return answer
        
    