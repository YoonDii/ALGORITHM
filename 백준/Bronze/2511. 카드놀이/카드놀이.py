a = list(map(int,input().split()))
b = list(map(int,input().split()))
acnt = 0
bcnt = 0
rec = "D"
for i in range(10):
    if a[i] > b[i]:
        acnt += 3
        rec = "A"
    if a[i] < b[i]:
        bcnt += 3
        rec = "B"
    if a[i] == b[i]:
        acnt += 1
        bcnt += 1
if acnt > bcnt:
    print(acnt, bcnt)
    print("A")
if acnt < bcnt:
    print(acnt, bcnt)
    print("B")
if acnt == bcnt:
    if rec == "A":
        print(acnt, bcnt)
        print("A")
    if rec == "B":
        print(acnt, bcnt)
        print("B")
    if rec == "D":
        print(acnt, bcnt)
        print("D")