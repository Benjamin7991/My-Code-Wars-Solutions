def spin_words(sentence):
    sentence = sentence.split()
    if len(sentence) < 2:
        for word in sentence:
            if len(word) > 5:
                word = word[::-1]
            return word
        
    else:
        list = []
        for word in sentence:
            if len(word) >= 5:
                new = word[::-1]
                list.append(new)
            else:
                list.append(word)
    return ' '.join(list)
