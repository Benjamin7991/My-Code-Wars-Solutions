def pseudo_sort(st): 
    st = st.split()
    new_st = []
    punct = ',.!?'
    
    for item in st:
        item = ''.join([x for x in item if x.isalpha()])
        new_st.append(item)
    
    result = ' '.join(new_st).strip()
    
    lower = []
    upper = []
    
    for item in result.split():
        if item[0]:
            if item[0].islower():
                lower.append(item)
            if item[0].isupper():
                upper.append(item)

    lower = sorted(lower)
    upper = sorted(upper)[::-1]
    result = lower + upper
    
    newest = ' '.join(result)
    return ' '.join(lower + upper)
