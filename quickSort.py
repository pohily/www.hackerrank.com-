def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    for elem in arr[1:]:
        if elem < p:
            left.append(elem)
        else:
            right.append(elem)
    return left+[p]+right

print(quickSort([4, 5, 3, 7, 2]))
