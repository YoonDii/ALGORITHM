import re
def solution(myString):
    return re.sub(r"[a-k]", "l", myString)