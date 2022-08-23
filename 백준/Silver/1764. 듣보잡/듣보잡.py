a , b = map(int,input().split())

dj = []
bj = []

for i in range(a):
    dj.append(input())
for i in range(b):
    bj.append(input())

# print(dj, bj) 
# ['ohhenrie', 'charlie', 'baesangwook'] 
# ['obama', 'baesangwook', 'ohhenrie', 'clinton']

dbj = sorted((set(dj)& set(bj)))
# print(dbj)

print(len(dbj))
for ans in dbj:
    print(ans)