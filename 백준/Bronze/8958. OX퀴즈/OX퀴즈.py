n = int(input())

for i in range(n):
    ox_list = list(input())  #list로 입력받기

    #OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
    cnt = 0
    ox_cnt = 0
    for ox in ox_list: 
        if ox == 'O':      #변수가 O라면
            cnt += 1       # 1을 더해준다.
            ox_cnt += cnt  # O가 연속되면 점수가 1점씩 커진다.
        else:       #아니면
            cnt = 0 #0점 추가

    print(ox_cnt)