chess = list(map(int,input().split()))

origin = [1,1,2,2,2,8]

for i in range(6):
    ans =  origin[i] - chess[i]
    print(ans,end=' ')