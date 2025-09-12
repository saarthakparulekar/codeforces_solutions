t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())

    solved = set()
    total = 0
    for c in s:
        if c not in solved:
            total += 1
            solved.add(c)
        total += 1
    print(total)