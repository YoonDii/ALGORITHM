T = int(input())

for i in range(T):
    PS = input()
    PS_li = []

    for x in PS:
        if x == '(':
            PS_li.append(')')
        if x == ')':
            if len(PS_li) == 0:
                PS_li.append(')')
                break
            else:
                PS_li.pop()
    if len(PS_li) != 0:
        print('NO')
    else:
        print('YES')