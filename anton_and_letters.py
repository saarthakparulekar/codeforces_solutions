s = str(input())
arr = s.replace('{', '').replace('}', '').replace(',', '').split()
print(len(set(arr)))