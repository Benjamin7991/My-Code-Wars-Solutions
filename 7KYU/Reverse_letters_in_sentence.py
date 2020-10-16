def reverser(sentence):
    reversed = ' '.join(w[::-1] for w in sentence.split())
    if sentence == ' ':
        return ' '
    if sentence == '  ':
        return '  '
    
    j = [x for x in reversed]
    

    for i in range(len(sentence)):
        if sentence[i] not in j:
            j.insert(i, sentence[i])

    if sentence[0] == ' ':
        j.insert(0, ' ')
    if sentence[-1] == ' ':
        j.insert( (len(sentence) -1), ' ')
        
    return ''.join(j)
