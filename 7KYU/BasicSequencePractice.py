def sum_of_n(n):
    
    list = [0]
    list2 = [0]
    
    if n < 0:
        n = abs(n)
        while len(list2) < abs(n+1):
            list2.append(len(list2) + list2[-1])
        return [-x for x in list2]
    
    if n == 0:
        return [0]
    
    if n > 0:
        while len(list) < abs(n+1):
            list.append(len(list) + list[-1])
        return list
