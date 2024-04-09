def solution(myString, pat):
    answer = "".join(["B" if char == "A" else "A" for char in myString])
    return 1 if pat in answer else 0