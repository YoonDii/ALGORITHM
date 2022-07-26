n = int(input())   #수열길이
arr = list(map(int,input().split()))  #수열받기

up = 0   #오르막길 크기
up_arr = []  #오르막길 길이측정

for i in range(1, n):
    if arr[i] > arr[i-1]:        #수열 1번째보다 2번째가 더 크면 / 앞길보다 뒷길이 크면
        up += arr[i] - arr[i-1]  #두값의 차를 오르막길 크기에 더해주기   # 1 2 3 ---> 1+1
        if i == n - 1:           
            up_arr.append(up)    #print(up_arr)  [1,5]

    else:                        #내리막길인 경우
        up_arr.append(up)        #0으로 계산하기
        up = 0
print(max(up_arr)) # 가장 큰 오르막길의 크기 출력