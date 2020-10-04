def solve(s):
    
    list = []
    numbers = range(1,27)
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string = ''
    vowels = 'aeiou'
    for char in s:
        if char in vowels:
            string += '-'
        else:
            string += char
    
    result = string.split('-')
    d = dict(zip(alpha, numbers))
    
    list = []
    for item in result:
        if item == '':
            result.remove(item)
    
    list2 = []
    for item in result:
        for char in item:
            item= [char for char in item]
        list2.append(item)
    
    list3 = []
    for item in list2:
        for char in item:
            if char in d:
                new = [d.get(char) for char in item]
        list3.append(sum(new))
    return max(list3)
