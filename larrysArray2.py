def larrysArray(A):
    count = 0
    for i, v in enumerate(A):
        x = A[i+1:]
        count += sum([1 for elem in x if elem < v])
    print(count)    
    if count % 2 == 1:
        return 'NO'
    else:
        return 'YES'

#print(larrysArray([3, 2, 1]))
print(larrysArray([9, 6, 8, 12, 3, 7, 1, 11, 10, 2, 5, 4]))
#print(larrysArray([17, 21, 2, 1, 16, 9, 12, 11, 6, 18,
#                   20, 7, 14, 8, 19, 10, 3, 4, 13, 5, 15]))   
















