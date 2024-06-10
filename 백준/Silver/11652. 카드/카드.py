import sys
input = sys.stdin.readline

dict_ = {}
N = int(input())
for i in range(N):
    card = int(input())
    
    if card in dict_.keys():
        dict_[card] += 1
    elif card not in dict_.keys():
        dict_[card] = 1
        
sorted_dict = sorted(dict_.items(), key = lambda x : (-x[1],x[0]))
print(sorted_dict[0][0])