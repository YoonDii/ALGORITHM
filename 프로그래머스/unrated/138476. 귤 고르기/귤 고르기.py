def solution(k, tangerine):
    answer = 0
    l= [0 for i in range(max(tangerine))]
    
    for i in range(len(tangerine)):
        l[tangerine[i]-1] += 1
    l.sort(reverse = True)

    index = 0
    while answer < k:
        answer += l[index]
        index += 1
    return index
    