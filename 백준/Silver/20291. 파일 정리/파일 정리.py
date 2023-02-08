n = int(input())

file = dict()
for i in range(n):
    extension = (input().split("."))[1]
    if extension in file:
        file[extension] += 1
    else:
        file[extension] = 1
sort_file = sorted(file.items())
# print(sort_file) [('icpc', 2), ('spc', 2), ('txt', 3), ('world', 1)]

for k, v in sort_file:
    print(k.rstrip(), v)