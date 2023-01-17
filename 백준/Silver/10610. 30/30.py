n = list((input()))
n.sort(reverse=True)  # 큰수가 먼저오게 정렬

sum = 0
for i in n:
    sum += int(i)

if (
    sum % 3 != 0 or "0" not in n
):  # 일의자리수가 0이여야하고, 각자리의 숫자들을 더했을대 3으로 나누어 떨어져야 30의 배수가 된다
    print(-1)
else:
    print("".join(n))
