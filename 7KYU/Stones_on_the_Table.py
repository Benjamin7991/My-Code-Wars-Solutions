def solution(stones):
    count = 0
    for i in range(len(stones)):
        try:
            if stones[i] == stones[i+1]:
                count += 1
                
        except:
            return count
