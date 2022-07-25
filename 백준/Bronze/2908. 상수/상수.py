a, b =input().split()

#첫글자와 마지막글자만 바꾸면 되니까 역순으로 추출
a = int(a[::-1]) #734  --> 437
b = int(b[::-1]) 

#둘 중 큰 수 출력
if a > b: 
    print(a)
else:
    print(b)
