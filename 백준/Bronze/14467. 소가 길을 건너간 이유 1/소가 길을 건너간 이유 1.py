n = int(input())#관찰횟수

cow = {} #소위치
cnt = 0

for i in range(n):
    a , b = map(int,input().split()) 
    if a in cow and cow[a] != b: # 소가 있으면 카운트, 없으면 딕셔너리에 저장.
        cnt += 1
    cow[a] = b
print(cnt) # 카운트만 출력
