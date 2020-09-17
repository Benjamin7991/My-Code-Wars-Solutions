def vowel_start(st): 
    st = st.split()
    st = ''.join(st)
    vowels = 'aeiou'
    ss = ''
    
    for char in st:
        if char.isalnum():
            ss += char
            ss = ss.lower()
    for char in ss:
        if char in vowels:
            ss = ss.replace(char, ' ' + char)
        ss= ss.strip()
    res = ss.split()
    return ' '.join(res)
