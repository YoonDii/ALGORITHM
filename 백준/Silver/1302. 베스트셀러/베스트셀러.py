n = int(input())

book = []
d = {}
best = []

for i in range(n):
    book.append(input())
    # print(book)

for j in set(book) :
    d[j] = book.count(j)
    # print(d[j])

for k in d.keys():
    if d[k] == max(d.values()):
        best.append(k)
        # print(best)

best.sort()
print(best[0])