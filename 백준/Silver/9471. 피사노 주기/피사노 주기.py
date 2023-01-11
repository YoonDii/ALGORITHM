t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    dp = [0, 1] #첫번째와 두번째는 고정. 주기확인을 위해
    cnt = 0 # 나머지가 0이 되기 전까지 더해준다.

    while True:
        dp.append((dp[-1] + dp[-2]) % m)
        cnt += 1
        if dp[-1] == 1 and dp[-2] == 0: #주기가 다 돌면 멈추기
            break

    print(i, cnt)