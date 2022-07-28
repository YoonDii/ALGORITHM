x, y = input().split()

x = int(x[::-1]) #123 -> 321
y = int(y[::-1]) #100 -> 1
#print(x,y) #321,1 

rev = x + y  #322
rev_li = str(rev) #str로 변환하여 list만들기

print((int(rev_li[::-1]))) #다시 int로 변환해서 추출

