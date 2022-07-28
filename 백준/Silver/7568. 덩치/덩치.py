n = int(input())

people = [] #list로 만들어서 비교할것임.
for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))  #인풋값 (x,y)로 넣기
    #print(people) #[(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]

for i in people : 
    rank = 1  #1등부터 나올수 있게 초기값은 1
    for x in people:
        if i[0] < x[0] and i[1] < x[1]: #각각 자리비교 조건
            #print(x)
            rank+=1 #조건 만족 시 count up
    print(rank, end = " ") #바로 출력