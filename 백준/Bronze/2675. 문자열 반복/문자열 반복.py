n = int(input())


for i in range(n):
  r,s = input().split()
  r = int(r)
  s = str(s)

  for i in range(len(s)):
    print(r*s[i],end ='')
  print()