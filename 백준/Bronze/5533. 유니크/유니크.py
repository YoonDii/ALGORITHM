n = int(input())
m = 3
num_lst = [list(map(int,input().split())) for _ in range(n)]
dic = {}
scores = []
for j in range(m):
    game_round = [num_lst[i][j] for i in range(n)]
    #print(game_round)
    same = [x for i,x in enumerate(game_round) if x in game_round[:i]]
    #print(same)
    for i in range(n):
        dic.setdefault(i,0)
        if game_round[i] in same:
            dic[i] += 0
        else : dic[i] += game_round[i]
print(*dic.values(),sep ='\n')
