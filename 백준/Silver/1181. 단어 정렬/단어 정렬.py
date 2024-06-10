
list_ = []
N = int(input())
for i in range(N):
    list_.append(input())

list_ = list(set(list_))

list_.sort()
list_.sort(key=len)

for i in list_:
    print(i)