import sys

A, B = map(int, sys.stdin.readline().split())
a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

# gcd
print(a)

#lcm
print(A*B//a)