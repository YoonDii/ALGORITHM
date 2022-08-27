n,m = map(int,input().split()) 
card = list(map(int,input().split()))
sum = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            summ = card[i]+card[j]+card[k]
            if summ <= m:
                sum.append(summ)
print(max(sum))
