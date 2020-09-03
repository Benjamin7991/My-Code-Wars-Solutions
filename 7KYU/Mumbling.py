def accum(s):
    s=s.lower()
    list = []
    for i in range(len(s)):
        total = s[i]*(i+1)
        list.append(total)
    return '-'.join(list).title()
       
