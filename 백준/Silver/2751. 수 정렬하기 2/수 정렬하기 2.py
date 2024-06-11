import sys
input=sys.stdin.readline
N = int(input())
list_ = []
for i in range(N):
    list_.append(int(input()))
list_.sort()
for i in list_:
    print(i)