def tidyNumber(n):
    n = str(n)
    li = []
    for i in range(len(n)):
        try:
            li.append(n[i] <= n[i+1])
            
        except:
            ''
    if False in li:
        return False
    else:
        return True
