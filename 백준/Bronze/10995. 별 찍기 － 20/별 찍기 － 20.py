n = int(input())

if n == 1:
    print('*')
    
else:
    for i in range(n):
        if i % 2 == 0: #짝수면 *뒤에 공백
            a = print('* ' * n)
        else:  #홀수면 *앞에 공백
            b = print(' *' * n)