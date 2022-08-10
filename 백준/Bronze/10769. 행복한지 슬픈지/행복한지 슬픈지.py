# 행복한 얼굴을 나타내는 :-) 
# 슬픈 얼굴을 나타내는 :-( 

txt = input()
a = txt.count(':-)')
b = txt.count(':-(')

if ':-)' not in txt and ':-(' not in txt:
    print('none')
elif a == b :
    print('unsure')
elif a > b :
    print('happy')
else:
    print('sad')