def is_matching(st, st1, st2): 
    total = st1 + st2
    total = ''.join([x for x in total]).lower()
    l = []
    st = st.lower()
    for item in ''.join(st.split()):
        if st.count(item) ==  total.count(item):
            l.append(True)
        else:
            l.append(False)
    
    if False in l:
        return False
    return True
