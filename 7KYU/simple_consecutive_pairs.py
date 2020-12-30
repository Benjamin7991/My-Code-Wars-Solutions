def pairs(ar):
    n = 2
    l = []
    count = 0
    for i in range(len(ar)):
        try:
            a = (ar[i], ar[i+1])
            l.append(a)
        except:
            pass
    zipped = zip(ar[0::2], ar[1::2])
    for item in list(zipped):
        if abs(item[1] - item[0]) == 1 or abs(item[0] - item[1]) == 1:
            count += 1
            
    return count
