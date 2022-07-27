word = input().upper() #출력은 대문자가 나와야 하기때문에 처음부터 대문자로 변환
word_li = list(set(word)) #문자열 각각의 개수를 구해야하기에 list로 변환

cnt_li = [word.count(i) for i in word_li]
# word_li에 있는 i가 word에 몇개 있는지 카운트해서 cnt_li를 만들어줘  

if cnt_li.count(max(cnt_li)) > 1: #만약 cnt_li에 max값을 카운트했는데 1보다 많으면
    print('?')    # ? 출력

else:
    max_index = cnt_li.index(max(cnt_li))  #cnt_li에서 가장 많이 있는 인덱스위치를 반환
    print(word_li[max_index])  #word_li에서 가장 많은 알파벳 출력
