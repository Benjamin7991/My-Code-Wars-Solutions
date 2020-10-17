def vowel_start(st):
    chars = '?_,.!@#$%^&*()\'-{}""[]/\<>;:`~|=+'
    vowels = ['a', 'e', 'i', 'o', 'u']
    test = ''.join([x for x in st.split()])
    result = ''
    
    for char in test.lower():
        if char in vowels:
            result += ' ' + char
        else:
            result += char
    
    return ''.join([x for x in result.strip() if x not in chars]).strip()
