
c = int(input())
f = int(input())

virus = [[] * (c+1) for i in range(c+1)] 
ans = [1]

for i in range(f): #인접 리스트
    u, v = map(int,input().split())
    virus[u].append(v)
    virus[v].append(u)
    #print(virus) #[[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

infection = True #감염여부
while infection:
    len_ans = len(ans)

    for i in ans:
        for j in virus[i]:
            if j not in ans:
                ans.append(j)
    if len(ans) == len_ans: #둘의 길이가 같은 감염안됌
        infection = False
print(len_ans -1) # virus의 처음은 빼야하기때문에 -1