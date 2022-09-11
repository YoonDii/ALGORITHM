word = input()
alphabet = list(range(97, 123))  # 아스키코드 숫자 범위 / a~z

for x in alphabet:
    print(word.find(chr(x))) # 알파벳을 숫자로 변환하여 출력