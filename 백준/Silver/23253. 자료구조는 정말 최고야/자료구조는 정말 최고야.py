n , m = map(int,input().split())

clean = True  #참/거짓으로 판별
for i in range(m):
    k = int(input())
    book = list(map(int,input().split())) #리스트로 변환하여 받는다.

    for b in range(k-1): # 책의 개수, 리스트로 받으니까 -1해줌 
        if book[b] < book[b+1]: # 앞수보다 뒷수가 더 크면 /...먼저오는 수가 더 큰수기때문에 [3 5 1] 이러면 false
            clean = False #거짓
            break
        if not clean: # 앞수가 더 크면 참
            break
if clean:
    print('Yes') #참이면 Yes
else:
    print('No') #거짓이면 No