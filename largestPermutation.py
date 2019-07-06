def largestPermutation(k, arr):
    curPosition = 0
    while k and curPosition != len(arr)-1:
        i = arr.index(max(arr[curPosition:]))
        if i != curPosition:
            arr[i], arr[curPosition] = arr[curPosition], arr[i]
            curPosition += 1
            k -= 1
        else: 
            curPosition += 1
    return arr
print(largestPermutation(1, [4, 2, 3, 5, 1]))




def largestPermutation(k, arr): #  с использованием индексного словаря, чтобы не искать максимум каждый раз, а брать его индекс из словаря по значению
    indArr = {}
    for i, v in enumerate(arr):
        indArr[v] = i
    curPosition = 0
    while k and curPosition != len(arr)-1:
        
        i = indArr[max(arr[curPosition:])]
        if i != curPosition:
            arr[i], arr[curPosition] = arr[curPosition], arr[i]
            indArr[arr[i]], indArr[arr[curPosition]] = indArr[arr[curPosition]], indArr[arr[i]]
            curPosition += 1
            k -= 1
        else: 
            curPosition += 1
    return arr
print(largestPermutation(1, [4, 2, 3, 5, 1]))






