import re

def uniq(seq):
    list= []
    other_list = []
    pattern = r'(.)\1+'
    
    if len(seq) == 1:
        return seq
    
    if None in seq:
        res =  ''.join(item for item in seq if item != None)
        res = re.sub(pattern, r'\1', res)
        for thing in res:
            other_list.append(None)
            other_list.append(thing)
        return other_list
            
        
    
    else:
        newseq = ''.join(seq)
        #pattern = r'(.)\1+'
        result = re.sub(pattern, r'\1', newseq)
        for item in result:
            list.append(item)
    return list    
    
