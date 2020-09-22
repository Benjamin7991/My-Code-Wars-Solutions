def name_value(my_list):
    list = []
    list2 =[]
    list3 = []
    list4 = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    enum = dict(enumerate(alphabet, 1))
    res = dict((v,k) for k,v in enum.items())
    
    for words in my_list:
        for letter in words:
            if letter in res:
                words = words.replace(letter, str(res.get(letter)) + ',')
        list.append(words)
    for item in list:
        item = item.split(',')
        list3.append(item)
    
    for items in list3:
        for char in items:
            if char == '':
                items.remove(char)
    
    x = [[int(float(j)) for j in i] for i in list3]
    for item in x:
        summed = sum(item)
        list4.append(summed)
    
    
    for i in range(len(list4)):
        list4[i] = list4[i] * (i+1)
    return list4
