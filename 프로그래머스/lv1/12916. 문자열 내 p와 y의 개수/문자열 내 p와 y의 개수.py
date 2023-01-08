def solution(s):

    s = s.lower()
    s1 = "p"
    s2 = "y"

    x = s.count(s1)
    y = s.count(s2)

    return (x == y)