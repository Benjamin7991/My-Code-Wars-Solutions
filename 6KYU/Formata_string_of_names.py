def namelist(names):
    names = [d['name'] for d in names]
    try:
        if len(names) > 1:
            last_item = names[-2] + ' & ' + names[-1] 
            names.insert(-1, last_item)
            names.pop()
            names.pop(-2)
            
    except:
        pass
    return ', '.join(names)
