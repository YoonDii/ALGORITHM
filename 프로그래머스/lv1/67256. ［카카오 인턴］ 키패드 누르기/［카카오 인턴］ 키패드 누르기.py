def solution(numbers, hand):
    answer = ''
    Left = 10
    Right = 12
    for n in numbers:
        # print(Left, Right)
        if n == 1 or n == 4 or n == 7:
            answer += "L"
            Left = n
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
            Right = n
        else:
            if n == 0:
                n = 11
            #왼쪽거리    
            L_dis = abs(Left-n) // 3 + abs(Left-n) % 3
            #오른쪽거리
            R_dis = abs(Right-n) // 3 + abs(Right-n) % 3
            
            if L_dis > R_dis:
                answer += "R"
                Right = n
            elif R_dis > L_dis:
                answer += "L"
                Left = n
            else:
                if hand == "right":
                    answer += "R"
                    Right = n
                else:
                    answer += "L"
                    Left = n
    return answer