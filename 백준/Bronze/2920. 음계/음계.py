nums = list(map(int,input().split()))

song = [1,2,3,4,5,6,7,8]

if nums == song :
    print('ascending')
elif nums == song[::-1]:
    print('descending')
else:
    print('mixed')