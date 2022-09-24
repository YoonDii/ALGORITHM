import sys
input=sys.stdin.readline

nums = []
n, k = map(int,input().split())
x = list(map(int,input().split()))

# print(x) [100, 76, 85, 93, 98]

x.sort(reverse=True)
# print(x) [100, 98, 93, 85, 76]

print(x[k-1])