def caesar_encode(phrase, shift):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    test = list(enumerate(phrase.split(), shift))


    for item in test:
        for letter in item[1]:
            if letter in alpha:
                index = alpha.index(letter)
                l.append(alpha[(index + item[0]) % 26])
            if letter not in alpha:
                l.append(' ')
                
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            l.insert(i, ' ')
    return ''.join(l)
