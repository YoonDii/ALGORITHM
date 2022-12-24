def solution(sizes):
    w = []
    h = []
    result = 0
    for i in range (len(sizes)):
        w.append(max(sizes[i]))
        # print(w)
        h.append(min(sizes[i]))
        # print(h)
    result = max(w) * max(h)
    return result
        