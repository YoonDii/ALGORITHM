a = int(input())
b = int(input())
c = int(input())

ans = list(str(a * b *c)) #곱한 값을 문자열로 변환하여 list로 반환

for i in range(10): # i = 0~9
    print(ans.count(str(i))) # list요소가 몇개인지 세기
# 3