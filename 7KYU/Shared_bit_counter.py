def shared_bits(a, b):
    a= bin(a)[2:]
    b = bin(b)[2:]
    
    if len(a) < len(b):
        a = a.zfill(len(b))
        
    if len(b) < len(a):
        b = b.zfill(len(a))
        
    count = 0
    
    for i in range(len(a)):
        try:
            if a[i] == '1' and b[i] == '1':
                count += 1
        except:
            pass
        
    return count >= 2
