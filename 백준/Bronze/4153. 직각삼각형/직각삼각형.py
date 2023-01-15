while True:
        a = list(map(int, input().split()))
        mnum = max(a)
        if sum(a) == 0:#마지막 0,0,0 을 위한 코드
                break
        a.remove(mnum) #제일긴변빼기 / 나머지 두개의 변 비교하기위해서
        if a[0] ** 2 + a[1] ** 2 == mnum ** 2: #피타고라스의정리
                print('right')
        else:
                print('wrong')