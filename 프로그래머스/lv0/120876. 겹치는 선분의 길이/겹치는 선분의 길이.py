def solution(lines):
    table = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a, b):
            table[i + 100].add(index)

    count = 0
    for line in table:
        if len(line) > 1:
            count += 1

    return count