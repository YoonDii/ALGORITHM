while True:
    letter = input().lower()
    if letter == '#':
        break
    cnt = 0
    for m in letter:
        if m in 'aeiou':
            cnt +=1
    print(cnt)