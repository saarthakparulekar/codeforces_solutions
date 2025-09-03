t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(0, n , 2):
        if i + 1 < n and arr[i] > arr[i+1]:
            diff = arr[i] - arr[i+1]
            arr[i] -= diff
            res += diff
        if i > 0 and arr[i] > arr[i-1]:
            diff = arr[i] - arr[i-1]
            arr[i] -= diff
            res += diff
        if i > 0  and (arr[i] + arr[i - 2]) > arr[i-1]:
            diff = (arr[i] + arr[i - 2]) - arr[i - 1]
            arr[i] -= diff 
            res += diff
    print(res)
