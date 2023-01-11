def solution(n, lost, reserve):
    a = set(reserve) - set(lost) #빌려줄수있는사람
    b = set(lost) - set(reserve)#도난당한사람

    for i in a:
        if i-1 in b: # i보다 왼쪽인사람이 도난당한사람에 있으면
            b.remove(i-1) #그 사람 제거
        elif i+1 in b: #i보다 오른쪽인사람이 도난당한사람에 있으면
            b.remove(i+1) # 그사람 제거
            #제거해주는 이유는 체육복을 빌려 수업을 들을 수 있기 때문에

    return n - len(b) #전체수에서 도난당한사람길이 빼기//수업들을 사람 구하기