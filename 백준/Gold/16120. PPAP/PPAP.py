word = input()
stack = []

if word == "P" or word == "PPAP":  # 기본조건에 맞춰 출력/ P는 PPAP 문자열이다 /PPAP는 PPAP 문자열이다.
    print("PPAP")
else:
    ppap = ["P", "P", "A", "P"]
    for i in word:  # 입력값을 돌면서 스택에 넣기
        stack.append(i)
        if stack[-4:] == ppap:  # 뒤에 4글자가 ppap면 P만 남기자
            # print(stack[-4:])['A', 'P', 'A', 'P']
            stack.pop()
            stack.pop()
            stack.pop()
    if stack == ppap or stack == ["P"]:  # 스택안에 요소가 ppap거나 P라면 PPAP출력
        print("PPAP")
    else:  # 아니라면 NP출력
        print("NP")