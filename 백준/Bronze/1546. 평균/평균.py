n = int(input())
sejun = list(map(int, input().split()))

m = max(sejun)

new_sj = []  # 새로운 리스트 구하기
for i in sejun:
    new_sj.append(i/m*100)  # 새로운 리스트에 넣어주기
    new_avg = sum(new_sj)/n  # 새로운평균
print(new_avg)
