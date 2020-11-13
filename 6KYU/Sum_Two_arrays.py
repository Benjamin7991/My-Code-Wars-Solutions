def sum_arrays(array1,array2):
    one = ''.join(str(x) for x in array1)
    two = ''.join(str(x) for x in array2)
    
    if array1 == [] and array2 == []:
        return []
    if array1 == []:
        return array2
    if array2 == []:
        return array1
    
    result = int(one) + int(two)
    
    li = []
    if str(result)[0] == '-':
        new = int(str(result)[0:2])    
        li.append(new)
        result = [int(x) for x in str(result)[2:]]
        for item in result:
            li.append(item)
        return li 
    else:
        return [int(x) for x in str(result)]
