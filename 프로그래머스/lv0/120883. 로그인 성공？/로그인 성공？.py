def solution(id_pw, db):
    answer = ''
    check = False
    # print(id_pw[0],id_pw[1])
    for i in range(len(db)):
        if db[i][0] == id_pw[0]:
            check = True
            if db[i][1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"
            
            
    