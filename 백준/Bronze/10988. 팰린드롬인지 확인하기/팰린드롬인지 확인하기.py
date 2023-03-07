word = input()

if word[0::] == word[::-1]:
    print(1)
else:
    print(0)