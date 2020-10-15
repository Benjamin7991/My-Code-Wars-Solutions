def next_letter(s):
    al = 'abcdefghijklmnopqrstuvwxyz'
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    
    for char in s:
        if char.lower():
            if char in al:
                i = al.index(char)
                new_i = al[(i+1) % 26]
                result.append(new_i)
        if char.upper():
            if char in cap:
                i = cap.index(char)
                new_i = cap[(i+1) % 26]
                result.append(new_i)
        
        if not char.isalpha():
            result.append(char)
    return ''.join(result)
