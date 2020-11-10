import re

def decipher_this(string):
    array = re.findall(r'[0-9]+', string)
    test = re.sub(r'[0-9]+', '_', string)
    new = [chr(int(x)) for x in array]
    dam = []
    boom = ''
    
    for item in test.split():
        if len(item) > 2:
            new_item = item[-1] + item[2:-1] + item[1]
            dam.append(new_item)
        else:
            dam.append(item)
    result = list(zip(new, dam))
    
    answer = ' '.join([item[0] + item[1] for item in result])
    
    for char in answer:
        if char != '_':
            boom+=char
    return boom
