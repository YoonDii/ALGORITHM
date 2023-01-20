n = int(input())
# no, no 중복제외하기 위해 set
w = set(input() for _ in range(n))
words = list(w)

# 사전 순으로 정렬
words.sort()
# print(words)
# 길이 순으로 정렬
words.sort(key=len)
# print(words)

for i in range(len(words)):
    print(words[i])