def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer=1111*a
    elif a==b==c:
        answer=(10*a+d)**2
    elif a==b==d:
        answer=(10*a+c)**2
    elif a==c==d: 
        answer=(10*a+b)**2
    elif b==c==d:
        answer=(10*d+a)**2
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    elif a==b:
        answer=c*d
    elif a==c:
        answer=b*d
    elif a==d:
        answer=b*c
    elif b==c:
        answer=a*d
    elif b==d:
        answer=a*c
    elif c==d:
        answer=a*b
    else:
        answer=min(a,b,c,d)
    return answer