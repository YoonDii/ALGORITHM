import sys
N=int(sys.stdin.readline())

list_ = []
for i in range(N):
    list_.append(list(map(int,sys.stdin.readline().split())))
    
#sorted_list = sorted(list_, key = lambda x : (x[1],x[0]))
list_.sort()
for i in list_:
    print(i[0],i[1])
    