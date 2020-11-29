def solve(arr):
    arr = sorted(arr)
    
    li = []
    result = []
    while arr:
        try:
            li.append(max(arr))
            li.append(min(arr))
            arr.remove(max(arr))
            arr.remove(min(arr))
        except:
            ''
    for item in li:
        if item not in result:
            result.append(item)
            
    return result
