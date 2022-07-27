mush = []
total = 0
for i in range(10):
    mush.append(int(input())) #버섯 10개 입력하기
for x in mush:
    total += x #버섯더하기
    #print(mush,total)
    if total >= 100:                        #total이 100보다 크거나 같으면
        if total - 100 > 100 - (total - x): #버섯을 먹은 후와 먹기 전의 값을 비교했을 때 버섯을 먹은 값이 더 크면
            total -= x                      #100에 더 가까운 숫자 나올때 멈추기.
        #print(total) #totoal값이 100을 넘은 후 부터 계속 나옴.
        break
print(total) #숫자가 하나만 나오게 출력