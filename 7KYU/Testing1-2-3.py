def number(lines):
    list = []
    for i in range(len(lines)):
        list.append(str(i+1) + ': ' + lines[i])
    return list
