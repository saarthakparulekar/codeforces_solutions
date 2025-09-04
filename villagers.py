t = int(input())
for _ in range(t):
    n = int(input())
    villagers = list(map(int, input().split()))

    res = 0
    villagers.sort(reverse=True)
    for i in range(0, n, 2):
        res += villagers[i]
    print(res)