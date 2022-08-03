import sys
input = sys.stdin.readline

n , m = map(int, input().split())
num = [list(map(int,input().split())) for _ in range(n)]
k = int(input())

for o in range(k):
    i,j,x,y = map(int,input().split())
    cnt = 0
    #1 ≤ i ≤ x ≤ N, 1 ≤ j ≤ y ≤ M 
    for w in range(i-1,x): #리스트는 0부터라서 -1을해줌.
        for z in range(j-1,y):
            cnt += num[w][z]
    print(cnt)