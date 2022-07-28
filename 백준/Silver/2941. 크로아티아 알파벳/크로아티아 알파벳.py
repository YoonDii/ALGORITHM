cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
sum = 0
for i in range(len(cro)):  # cro를 읽어서
    c = word.count(cro[i]) # word에서 cro[i]의 수를 세기
    word = word.replace(cro[i],' ') # cro[i]에 해당하면 ' '로 치환
    sum += c  # cro[i]의 갯수 합의 총합
word = word.replace(' ','') # 공백제거
print(sum+len(word)) # cro에 없는 알파벳은 그냥 문자,갯수 세서 더해주기