def proofread(string):
    
    result = []
    string = string.lower().split()

    
    for word in string:
        if 'ie' in word:
            new_word = word.replace('ie', 'ei')
            result.append(new_word)
        else:
            result.append(word)
            
    test = ' '.join(result)
    test = test.split('.')
    
    final = []
    for item in test:
        item = item.strip().capitalize()
        final.append(item)
    return '. '.join(final).strip()
    
