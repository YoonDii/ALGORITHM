t = list(map(int,input().split()))

sing = [1,2,3,4,5,6,7,8]

if t == sing:
    print('ascending')
elif t == sing[::-1]:
    print('descending')
else:
    print('mixed')
