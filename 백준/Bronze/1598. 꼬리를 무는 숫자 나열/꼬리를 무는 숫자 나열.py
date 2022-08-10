a, b = map(int,input().split())

a -= 1
b -= 1

w = abs(a//4 - b//4)
h = abs(a % 4 - b % 4)
print(w+h)