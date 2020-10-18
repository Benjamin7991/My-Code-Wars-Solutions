def duplicate_sandwich(arr):
    dict = {}
    
    for char in arr:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    
    for k in dict:
        if dict.get(k) == 2:
            indices = [i for i, x in enumerate(arr) if x == k]
    return arr[(indices[0]+1):(indices[1])]
