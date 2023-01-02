# SWEA문제 5162번

tc = int(input())

for i in range(1, tc+1):
    a,b,c = map(int,input().split())

    if a < b : #a가 b보다 작으면
        answer = c // a
    else:
        answer = c // b
    print(f'#{i} {answer}')
