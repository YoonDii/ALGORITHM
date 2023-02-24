n, m = map(int, input().split())
cards = list(map(int, input().split()))

pick = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            card = cards[i] + cards[j] + cards[k]
            if card <= m:
                pick.append(card)
print(max(pick))