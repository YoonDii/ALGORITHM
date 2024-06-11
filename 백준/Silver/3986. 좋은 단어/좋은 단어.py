N = int(input())

count = 0
for i in range(N):
    s = input()
    list_ = []

    for x in s:
        if len(list_) == 0 :
            list_.append(x)
        else:
            if x == 'A' :
                if list_[-1] == 'B':
                    list_.append(x)
                elif list_[-1] == 'A':
                    list_.pop()
            elif x == 'B':
                if list_[-1] == 'A':
                    list_.append(x)
                elif list_[-1] == 'B':
                    list_.pop()
    if len(list_)== 0:
        count +=1
print(count)