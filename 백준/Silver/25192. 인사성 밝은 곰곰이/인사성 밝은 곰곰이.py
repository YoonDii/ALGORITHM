n = int(input())
userli = [input() for _ in range(n)]
slogin = set()
gom = 0

for user in userli:
    if user == 'ENTER':
        slogin.clear()
    else:
        if user not in slogin:
            slogin.add(user)
            gom += 1
print(gom)
