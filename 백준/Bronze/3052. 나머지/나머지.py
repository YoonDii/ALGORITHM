num = []
for _ in range(10):
    a= int(input())
    b = a % 42
    num.append(b)
    #print(num) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = set(num) #중복제거
#print(num2) 
print(len(num2)) # list요소의 개수를 구하는 방법은 길이구하기.