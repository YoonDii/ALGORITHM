import sys
letter, alph = sys.stdin.read(), [0 for i in range(26)]

for s in letter:
    if s.islower(): 
        alph[ord(s)-97] += 1 
           
for i in range(26):
    if alph[i] == max(alph):
        print(chr(i+97), end='')