t = int(input())

for x in range(1,t+1):
    class_n = list(map(int,input().split()))

    n = class_n[0]
    n_li = sorted(class_n[1:],reverse=True)
    #print(n_li)
    min_ = n_li[-1]
    max_ = n_li[0]
    gap = max([n_li[i] - n_li[i+1] for i in range(n-1)])
    #print(gap)

    print("Class",x)
    print(f"Max {max_}, Min {min_}, Largest gap {gap}")
