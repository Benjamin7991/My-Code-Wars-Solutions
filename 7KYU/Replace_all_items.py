def replace_all(obj, find, replace):
    r=[]
    for item in obj:
        if item == find:
            r.append(replace)
        else:
            r.append(item)
            
    if type(obj) == str:
        return ''.join(r)
    if type(obj) == list:
        return r
