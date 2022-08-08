hobit_list = []
for _ in range(9):
    hobit_list.append(int(input()))

sum_hobit = sum(hobit_list)

for a in range(8):
    for b in range(a + 1, 9):
        if sum_hobit - (hobit_list[a] + hobit_list[b]) == 100:
            hobit_list.remove(hobit_list[a])
            hobit_list.remove(hobit_list[b - 1])
            hobit_list.sort()
            break
    if len(hobit_list) < 9:
        break
for _ in hobit_list:
    print(_)