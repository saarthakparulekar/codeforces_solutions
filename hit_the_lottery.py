cash = int(input())
bills = [100, 20, 10, 5, 1]
res = 0
i = 0
while i < len(bills) and cash > 0:
    if bills[i] <= cash:
        change = cash // bills[i]
        res += change
        cash -= (bills[i] * change)
    else:
        i += 1

print(res)
        
