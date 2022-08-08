n = int(input())
seat = list(map(int,input().split()))
cnt = len(set(seat))
print(n - cnt)