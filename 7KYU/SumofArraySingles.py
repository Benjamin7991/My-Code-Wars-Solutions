def repeats(arr):
    list = []
    for num in arr:
        if arr.count(num) < 2:
            list.append(num)
    return sum(list)
