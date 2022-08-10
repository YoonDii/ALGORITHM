#리스트로받기
ws = [int(input()) for _ in range(10)] # [23, 23, 20, 15, 15, 14, 13, 9, 7, 6]
ks = [int(input()) for _ in range(10)] # [25, 19, 17, 17, 16, 13, 12, 11, 9, 5]

#내림차순으로정렬
sws = sorted(ws,reverse=True) # [23, 23, 20, 15, 15, 14, 13, 9, 7, 6] 
sks = sorted(ks,reverse=True) # [25, 19, 17, 17, 16, 13, 12, 11, 9, 5]

#높은점수3명의 합구하기
win_w = sum(sws[0:3])
win_k = sum(sks[0:3])

print(win_w, win_k)