n = int(input())
cnt = 0

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new = word[j+1:]
            if word[j] in new:
                cnt -= 1
                break
    cnt += 1

print(cnt)