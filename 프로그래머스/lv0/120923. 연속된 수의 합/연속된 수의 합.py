def solution(num, total):
    answer = []
    cnt = 0
    
    for i in range(1,num):
        cnt += i
    
    number = int((total-cnt)/num) # 첫번째 수찾기
    # print(number)
    
    for i in range(0,num):
        answer.append(number + i ) #처음수에 순차적으로 더하기/ 오름차순정렬까지
    return answer