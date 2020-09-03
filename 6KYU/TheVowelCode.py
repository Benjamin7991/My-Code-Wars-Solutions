dict1 = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u' : '5'}
dict2 = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5':'u'}

def encode(st):
    st = str(st)
    for char in st:
        if char in dict1:
            st = st.replace(char, dict1.get(char))
    return st
    
    

def decode(st):
    st = str(st)
    for char in st:
        if char in dict2:
            st = st.replace(char, dict2.get(char))
    return st 
