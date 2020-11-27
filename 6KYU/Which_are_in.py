def in_array(array1, array2):
    l = []
    new_l = []
    m = ''.join([x for x in array2])
    
    for item in array1:
        if item in m:
            l.append(item)
            
    l = sorted(l)
    
    for item in l:
        if item not in new_l:
            new_l.append(item)
    return new_l
