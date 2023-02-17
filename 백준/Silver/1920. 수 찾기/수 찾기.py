n = int(input())
arr = set(map(int, input().split()))
m = int(input())
search_list = list(map(int, input().split()))

for i in search_list:
    if i in arr:
        print(1)
    else:
        print(0)
