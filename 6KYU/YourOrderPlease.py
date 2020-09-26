def order(sentence):
    result = []
    list = []
    for char in sentence:
        if char.isnumeric():
            list.append(char)
    sentence = sentence.split()
    diction = dict(zip(list,sentence))
    od = sorted(diction.items())
    
    for item in od:
        result.append(item[1])
    return ' '.join(result)
