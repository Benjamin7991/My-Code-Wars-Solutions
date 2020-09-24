def encrypt_this(text):
    list = []
    res = []
    text = text.split()
    
    
    for word in text:
        if len(word) > 2:
            word = word[0] + word[-1] + word[2:-1] + word[1]
            list.append(word)
        else:
            list.append(word)
    
    for word in list:
        new = str(ord(word[0]))
        res.append(new + word[1:]) 
    return ' '.join(res)
