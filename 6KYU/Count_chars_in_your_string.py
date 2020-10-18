def count(string):
    dict = {}
    
    for char in string:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict
