std = [i for i in range(1,31)]

for _ in range(28):
    n = int(input())
    std.remove(n)
print(min(std))
print(max(std))