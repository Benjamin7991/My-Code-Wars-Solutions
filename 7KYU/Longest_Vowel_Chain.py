import re

def solve(s):
    pattern = r'([aeiou]+)'
    lens = []
    
    result = re.findall(pattern, s)
    
    for item in result:
        length = len(item)
        lens.append(length)
        
    return max(lens)
