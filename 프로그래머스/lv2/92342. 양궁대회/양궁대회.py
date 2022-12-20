def solution(n, info):
    result = []
    cnt = 0
    for i in range(1, 1024):
        a = bin(i)[2:]
        while len(a) < 10:
            a = "0" + a
        a = a[::-1]
        temp = [0,0,0,0,0,0,0,0,0,0,0,]#빈통
        for j in range(10):
            if a[j] == "1":
                temp[j] = info[j]+1
        lie = 0
        ape = 0

        for j in range(10):
            if temp[j] > info[j]:
                lie += 10-j
            elif temp[j] == 0 and info[j] == 0:
                continue
            elif temp[j] < info[j]:
                ape += 10-j
        if sum(temp) > n :
            continue #화살수가 크면 어차피 못쏨
        elif sum(temp) < n :
            temp[10] = n - sum(temp)

        if lie - ape >= cnt :
            cnt = lie - ape
            result = temp

    if cnt == 0 :
        return [-1]
    else :
        return result
