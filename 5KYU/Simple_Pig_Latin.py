def pig_it(text):
    text = text.split()
    punct = ['!', '?']
    
    
    result = []
    
    for word in text:
        word = word[1:] + word[0] + 'ay'
        result.append(word)
    final =  ' '.join(result)
    
    if '?' in final or '!' in final:
            for i in range(len(final)):
                if final[i] == '?' or final[i] == '!':
                    return final[:i] + final[i]
    else:
        return final
