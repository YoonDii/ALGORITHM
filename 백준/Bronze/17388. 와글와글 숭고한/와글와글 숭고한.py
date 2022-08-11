skh = list(map(int,input().split()))

if sum(skh) >= 100:
    print('OK')

if sum(skh) < 100:
    if min(skh) == skh[0]:
        print('Soongsil')
    elif min(skh) == skh[1]:
        print('Korea')
    else:
        print('Hanyang')