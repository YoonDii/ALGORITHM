while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n): # for문을 돌려서 약수 구하기
        if n % i == 0:
            arr.append(i) #빈리스트에 약수넣어주기
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")