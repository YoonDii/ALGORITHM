t = int(input())

for tc in range(1,t+1):
    n = int(input())
    buy = list(map(int,input().split()))
    sale = buy[-1]
    #print(sale)
    cnt = 0
    for i in range(len(buy)-1,-1,-1): #범위는 뒤에서부터 -1씩만큼 본다.
        if sale > buy[i]: # 파는날가격이 사는 날가격보다 크면
            cnt += sale - buy[i] #파는가격에서 산사격을 빼서 더해라
        else: #가격이 같거나 사는날이 더 비쌀땐 안더함.
            sale = buy[i]
    print(f'#{tc} {cnt}')