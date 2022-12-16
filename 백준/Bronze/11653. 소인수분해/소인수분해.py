n = int(input())
d = 2
while n != 1:
    if n%d == 0:
        n = n // d
        print(d)
    else:
        d+=1