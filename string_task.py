inputstr = list(str(input()).lower())
vowels = 'aeiouy'
res = ''
for c in inputstr:
    if c not in vowels:
        res += '.'
        res += c
print(res)