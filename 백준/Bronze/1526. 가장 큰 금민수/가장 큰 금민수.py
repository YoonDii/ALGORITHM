n = int(input())

while True:
    cnt = False
    for i in str(n):
        if i != '4' and i != '7':
            cnt = True
            n -= 1
           
    if cnt == 0:
        print(n)
        break