t = int(input())
for _ in range(t):
    [k, x] = list(map(int, input().split()))
    print(x * (2 ** k))