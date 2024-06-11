K = int(input())
stk = []
for i in range(K):
    m = int(input())

    if m != 0:
        stk.append(m)
    elif m == 0:
        stk.pop()
print(sum(stk))
