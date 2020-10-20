from itertools import cycle

def swap(s,n):
    n = bin(n)[2:]
    new = ''.join([x for x in s if x.isalpha()])
    sheet = list(zip(new,cycle(n)))
    result = []

    for item in sheet:
        if item[1] == '1':
            result.append(item[0].swapcase())
        else:
            result.append(item[0])
    
    for i in range(len(s)):
        if s[i].isnumeric() or not s[i].isalpha():
            result.insert(i, s[i])
    return ''.join(result)
