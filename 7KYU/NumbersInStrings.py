def solve(s):
    list2 = []
    for char in s:
        if char.isalpha():
            s=s.replace(char, ',')
    list = s.split(',')
    for item in list:
        if item != '':
            item = int(item)
            list2.append(item)
    return max(list2)
