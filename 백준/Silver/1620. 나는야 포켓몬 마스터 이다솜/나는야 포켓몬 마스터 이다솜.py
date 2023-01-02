n, m = map(int,input().split())

en = {}
num = {}
for i in range(1, n+1):
    name = input()
    en[name] = i # 키가 영어
    num[str(i)] = name # 키가 숫자
# print(en,num) 

for x in range(m):
    name = input()
    if name.isalpha(): #알파벳이면 키가 알파벳인 딕셔너리에서 숫자뽑기
        print(en[name])
    else:
        print(num[name]) # 알파벳이 아니면 키가 숫자인 딕셔너리에서 영어뽑기
