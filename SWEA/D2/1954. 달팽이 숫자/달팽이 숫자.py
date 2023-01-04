T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
 
    i, j, cnt, dr = 0, 0, 1, 0 # 초기화
    arr[i][j] = cnt
    cnt += 1
 
    while cnt <= N*N:
        ni, nj = i+di[dr], j+dj[dr]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
            i, j = ni, nj
            arr[i][j]=cnt
            cnt+=1
        else:
            dr = (dr+1)%4
 
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)