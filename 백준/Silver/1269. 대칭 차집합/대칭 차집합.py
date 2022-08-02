a , b = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

s_A = set(A)
s_B = set(B)

AA = len(s_A - s_B)
#print(AA)

BB = len(s_B - s_A)
#print(BB)


print(AA + BB)