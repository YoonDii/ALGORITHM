from collections import deque


t = int(input())
card = deque(range(1, t+1))

#print(card)    

while len(card) > 1:
   print(card.popleft(), end =' ')
   card.append(card.popleft())
    
print(card[0])