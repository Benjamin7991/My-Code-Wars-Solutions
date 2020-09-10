def clean_string(s):
    list = []
    for i in range(len(s)):
        if s[i] != '#':
            list.append(s[i])
        else:
            if (list != []):
                list.pop()
    return ''.join(list)
