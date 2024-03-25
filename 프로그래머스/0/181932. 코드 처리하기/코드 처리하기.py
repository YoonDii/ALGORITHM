def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"