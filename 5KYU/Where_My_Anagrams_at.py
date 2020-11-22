from collections import Counter

def anagrams(word, words):
    og_count=Counter(word) 
    
    l = []
    
    for item in words:
        if dict(Counter(item)) == og_count:
            l.append(item)
    return l
