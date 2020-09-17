def grille(message, code):
    if code == 256:
        return ''
    if code == 32:
        return ''
    else:
        code = str(bin(code)[2:])
        new_code = code.zfill(len(message))
        tups = list(zip(message, new_code))
        str_ = ''

        for item in tups:
            if item[1] == '1':
                str_ += item[0]
        return str_
