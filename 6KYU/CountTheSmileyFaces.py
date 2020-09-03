def count_smileys(arr):
    smiles = [':)',':D' , ';)' , ';D' , ':-)' , ';-)' , ':~)' , ';~)' , ':~D' , ';-D', ';~D', ':-D' ]
    count = 0
    for words in arr:
        if words in smiles:
            count += 1
    return count
