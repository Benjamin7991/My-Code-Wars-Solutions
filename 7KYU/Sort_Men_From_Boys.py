def men_from_boys(arr):

    even= sorted([x for x in arr if x % 2 ==0])
    odd = sorted([x for x in arr if x % 2 != 0])[::-1]
    result = []
            
    for item in even + odd:
        if item not in result:
            result.append(item)
            
    return result
