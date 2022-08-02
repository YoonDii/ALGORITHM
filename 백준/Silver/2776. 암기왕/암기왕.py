t = int(input())
for _ in range(t):
    n = int(input())
    n1 = set(map(int,input().split()))
    #print(n1) #{1, 2, 3, 4, 5}

    m = int(input())
    m2 = list(map(int,input().split())) 
    #print(m2) #[1, 3, 7, 9, 5]

    for i in m2:
        if i in n1:
            print(1)
        else:
            print(0)